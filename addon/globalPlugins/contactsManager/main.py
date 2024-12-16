# -*- coding: UTF-8 -*-

# Description:
# Lists all contacts registered in the phonebook.

# Author: Edilberto Fonseca
# Email: <edilberto.fonseca@outlook.com>
# Copyright (C) 2022-2025 Edilberto Fonseca
# This file is covered by the GNU General Public License.
# See the file COPYING for more details or visit https://www.gnu.org/licenses/gpl-2.0.html.

# Date of creation: 30/11/2022.

# Imports necessary for the add-on to function.
import logging
import os

import addonHandler
import config
import gui
import queueHandler
import ui
import wx
from gui import guiHelper

from . import controller as core
from .addEditRecord import AddEditRecDialog
from .varsConfig import ourAddon

# Get a logger with the name of the current module
logger = logging.getLogger(__name__)

# Add directories to sys.path before importing libraries
baseDir = os.path.dirname(__file__)
libs = os.path.join(baseDir, "lib")
try:
	from ObjectListView import ColumnDefn, ObjectListView
except ImportError as e:
	logger.error(f"Error importing module: {str(e)}")

# Initializes the translation
addonHandler.initTranslation()

# Get the title of the addon defined in the summary.
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]


class ContactList(wx.Dialog):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(ContactList, cls).__new__(cls, *args, **kwargs)
		else:
			msg = _("An instance of {} is already open.").format(ADDON_SUMMARY)
			queueHandler.queueFunction(queueHandler.eventQueue, ui.message, msg)
		return cls._instance

	def __init__(self, parent, title):
		if hasattr(self, "initialized"):
			return
		self.initialized = True

		# Title of contact list dialog.
		self.title = title

		WIDTH = 900
		HEIGHT = 450

		try:
			self.contactResults = core.get_all_records()
		except EOFError:
			self.contactResults = []

		super(ContactList, self).__init__(
			parent, title=title, size=(WIDTH, HEIGHT), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

		# Creating the screen objects.
		panel = wx.Panel(self)
		self.contactList = ObjectListView(panel, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
		wx.CallAfter(self.initialize_contact_list)
		self.contactList.SetFocus()

		# Translators: Message displayed when the contactList is empty.
		self.contactList.SetEmptyListMsg(_("No records found!"))

		# Translators: Search field label.
		labelSearch = wx.StaticText(panel, label=_('Search for: '))

		# List of combobox choices option.
		listOfOptions = [_('Name'), _('Cell phone'), _('Landline'), _('Email')]
		self.comboboxOptions = wx.ComboBox(panel, value=_('Name'), choices=listOfOptions)

		self.search = wx.SearchCtrl(panel, -1, size=(250, 25))
		self.buttonSearch = wx.Button(panel, label=_('&Search'))

		self.buttonEdit = wx.Button(panel, wx.ID_EDIT, label=_('&Edit'))
		self.buttonNew = wx.Button(panel, wx.ID_NEW, label=_('&New'))
		self.buttonDelete = wx.Button(panel, wx.ID_DELETE, label=_('&Remove'))
		self.buttonRefresh = wx.Button(panel, -1, label=_('Refres&h'))
		self.buttonImport = wx.Button(panel, -1, label=_('&Import csv...'))
		self.buttonExport = wx.Button(panel, -1, label=_('Ex&port csv...'))
		self.buttonResetRecords = wx.Button(panel, -1, label=_('&Delete all records.'))
		self.buttonExit = wx.Button(panel, wx.ID_CANCEL, label=_('E&xit'))
		self.set_config()

		# Creating the layout and adding it to the panel.
		boxSizer = wx.BoxSizer(wx.VERTICAL)
		viewSizer = wx.BoxSizer(wx.VERTICAL)
		searchSizer = wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		viewSizer.Add(self.contactList, 0, wx.ALL | wx.EXPAND, 5)
		searchSizer.Add(labelSearch, 0, wx.ALL, 5)
		searchSizer.Add(self.comboboxOptions, 0, wx.ALL, 5)
		searchSizer.Add(self.search, 1, wx.ALL, 5)
		searchSizer.Add(self.buttonSearch, 0, wx.ALL, 5)

		buttonSizer.Add(self.buttonEdit, 0, wx.ALL | wx.EXPAND, 5)
		buttonSizer.Add(self.buttonDelete, 0, wx.ALL | wx.EXPAND, 5)
		buttonSizer.Add(self.buttonRefresh, 0, wx.ALL | wx.EXPAND, 5)
		buttonSizer.Add(self.buttonImport, 0, wx.ALL | wx.EXPAND, 5)
		buttonSizer.Add(self.buttonExport, 0, wx.ALL | wx.EXPAND, 5)
		buttonSizer.Add(self.buttonResetRecords, 0, wx.ALL | wx.EXPAND, 5)
		buttonSizer.Add(self.buttonExit, 0, wx.ALL | wx.EXPAND, 5)

		# Define the main layout of the window
		boxSizer.Add(searchSizer, wx.ALL, guiHelper.BORDER_FOR_DIALOGS)
		boxSizer.Add(viewSizer, wx.ALL, guiHelper.BORDER_FOR_DIALOGS)
		boxSizer.Add(buttonSizer, 0, wx.CENTER)
		panel.SetSizerAndFit(boxSizer)
		self.Fit()

		# Binding events to buttons.
		self.buttonSearch.Bind(wx.EVT_BUTTON, self.onSearch, self.buttonSearch)
		self.buttonEdit.Bind(wx.EVT_BUTTON, self.onEdit, self.buttonEdit)
		self.buttonNew.Bind(wx.EVT_BUTTON, self.onNew, self.buttonNew)
		self.buttonDelete.Bind(wx.EVT_BUTTON, self.onDelete, self.buttonDelete)
		self.buttonRefresh.Bind(wx.EVT_BUTTON, self.onToUpdate, self.buttonRefresh)
		self.buttonImport.Bind(wx.EVT_BUTTON, self.onToImport, self.buttonImport)
		self.buttonExport.Bind(wx.EVT_BUTTON, self.onToExport, self.buttonExport)
		self.buttonResetRecords.Bind(wx.EVT_BUTTON, self.onReset, self.buttonResetRecords)
		self.buttonExit.Bind(wx.EVT_BUTTON, self.onClose, self.buttonExit)

	# Creating the columns of the ObjectListView.
	def initialize_contact_list(self):
		self.contactList.SetColumns([
			ColumnDefn(_('Name'), 'left', 250, 'name'),
			ColumnDefn(_('Cell phone'), 'right', 100, 'cell'),
			ColumnDefn(_('Landline'), 'right', 100, 'landline'),
			ColumnDefn(_('Email'), 'left', 200, 'email')
		])
		self.contactList.SetObjects(self.contactResults)

	# Show all records.
	def show_all_records(self):
		self.contactResults = core.get_all_records()
		self.initialize_contact_list()
		self.contactList.SetFocus()

	# Add a new record to the agenda.
	def onNew(self, event):
		dlg = AddEditRecDialog(gui.mainFrame)
		gui.mainFrame.prePopup
		dlg.ShowModal()
		dlg.CentreOnScreen()
		dlg.Destroy()
		gui.mainFrame.postPopup
		wx.CallAfter(self.show_all_records)
		self.contactList.SetFocus()

	# Edit a selected record.
	def onEdit(self, event):
		selectedRow = self.contactList.GetSelectedObject()
		if selectedRow is None:
			self.show_message(_('No records selected!'), _('Error'))
			return
		dlg = AddEditRecDialog(
			gui.mainFrame,
			selectedRow,
			title=_('To edit'),
			addRecord=False
		)
		gui.mainFrame.prePopup
		dlg.ShowModal()
		dlg.CentreOnScreen()
		dlg.Destroy()
		gui.mainFrame.postPopup
		wx.CallAfter(self.show_all_records)
		self.contactList.SetFocus()

	def onDelete(self, event):
		"""
		Deletes the selected record in the contact list after user confirmation.

		Args:
			event (wx.Event): The event that triggered this function.
		"""
		selectedRow = self.contactList.GetSelectedObject()
		if selectedRow is None:
			self.show_message(_('No records selected!'), _('Error'))
			return

		message = _('Do you want to delete the selected record?')
		caption = _('Attention')

		user_response = gui.messageBox(message, caption, style=wx.ICON_QUESTION | wx.YES_NO)
		if user_response == wx.YES:
			try:
				core.delete(selectedRow.id)
				self.show_message(_('Record deleted!'), _('Success'))
				self.show_all_records()
				self.contactList.SetFocus()
			except Exception as e:
				self.show_message(_('Error deleting record: {}').format(str(e)), _('Error'))
				return
		self.contactList.SetFocus()

	# Search using all the fields of the agenda.
	def onSearch(self, event):
		# Gets the chosen filter option and the entered keyword
		filterChoice = self.comboboxOptions.GetValue()
		keyword = self.search.GetValue()

		# Try to search based on filter and keyword option
		try:
			# Call the search function in the core module, passing the filter and keyword option
			self.contactResults = core.search_records(filterChoice, keyword)

			# Check if there were any results returned by the search
			if not self.contactResults:
				# If there are no results, displays an informative message
				self.show_message(_("No contacts found matching the search criteria."))
				self.search.SetFocus()
			else:
				# Otherwise, update the contact list in the graphical interface
				wx.CallAfter(self.initialize_contact_list())

				# Clear the search field after searching
				self.search.Clear()

				# Sets focus back to the contact list for easier navigation
				self.contactList.SetFocus()
		except Exception as e:
			# Display an error message if an exception occurs during the search
			self.show_message(_(f"{e}"))

	# Show all records in the ObjectListview's view control.
	def onToUpdate(self, event):
		ui.message(_("Updated records!"), True)
		self.show_all_records()
		wx.CallAfter(self.Show)

	# Import csv file to the agenda.
	def onToImport(self, event):
		dlg = wx.FileDialog(
			self, _('import csv file'),
			os.getcwd(), '', '*.csv', wx.FC_OPEN
		)
		if dlg.ShowModal() == wx.ID_OK:
			try:
				mypath = dlg.GetPath()
				core.import_csv_to_db(mypath)
				self.show_message(_('File imported successfully!'), _('Attention'))
				self.contactList.SetFocus()
			except Exception as e:
				msg = _(
					f'''It was not possible to import the file! {e}'''
				)

				# Translators: Message displayed to the user in case of errors when importing the CSV file
				self.show_message(msg, _('Attention'))
		dlg.Destroy()
		self.show_all_records()
		self.contactList.SetFocus()

	# Export the calendar to csv.
	def onToExport(self, event):
		dlg = wx.FileDialog(
			self,
			_('export csv file'),
			os.getcwd(),
			'agenda',
			'*.csv',
			wx.FD_SAVE
		)
		if dlg.ShowModal() == wx.ID_OK:
			try:
				mypath = dlg.GetPath()
				core.export_db_to_csv(mypath)
				self.show_message(_('File exported successfully!'), _('Attention'))
				self.contactList.SetFocus()
			except Exception as e:
				msg = _(
					f'''It was not possible to export the file! {e}'''
				)

				# Translators: Message displayed to the user in case of errors when exporting the CSV file
				self.show_message(msg, _('Attention'))
		dlg.Destroy()
		self.show_all_records()
		self.contactList.SetFocus()

	# Clear all the agenda.
	def onReset(self, event):
		"""
		Resets all phonebook records after user confirmation.

		Args:
			event (wx.Event): The event that triggered this function.
		"""

		try:
			selectedRow = core.count_records()
		except Exception as e:
			self.show_message(_('Error counting records: {}').format(str(e)), _('Error'))
			return

		if selectedRow == 0:
			self.show_message(_('The agenda is empty!'), _('Attention'))
			return

		message = _('This operation erases all phonebook entries. do you wish to continue?')
		caption = _('Attention')

		user_response = gui.messageBox(message, caption, style=wx.ICON_QUESTION | wx.YES_NO)
		if user_response == wx.YES:
			try:
				core.reset_record()
				self.show_message(_('Agenda deleted!'), _('Success'))
			except Exception as e:
				self.show_message(_('Error deleting records: {}').format(str(e)), _('Error'))
				return
		self.show_all_records()
		self.contactList.SetFocus()

	def set_config(self):
		"""
		Apply configurations specific to the add-on
		"""
		if config.conf[ourAddon.name]["resetRecords"] is False:
			self.buttonResetRecords.Disable()
		if (config.conf[ourAddon.name]["importCSV"] is False) or (config.conf[ourAddon.name]["exportCSV"] is False):
			self.buttonExport.Disable()
			self.buttonImport.Disable()

	def show_message(self, message, caption=_("Message"), style=wx.OK | wx.ICON_INFORMATION):
		"""
		Displays a message to the user in a dialog box.

		Args:
			message (str): The message to be displayed.
			caption (str, optional): The title of the dialog box. The default is ("Message").
			style (int, optional): The style of the dialog box,
			combining flags like wx.OK,
			wx.CANCEL, wx.ICON INFORMATION, etc. The default is wx.OK | wx.ICON INFORMATION.
		"""
		gui.messageBox(message, caption, style)

	def onKeyPress(self, event):
		"""
			Handles key press events in the dialog, closing it when Esc is pressed,
			deleting a link when Delete is pressed, and allowing editing of a link when F2 is pressed.

		Args:
			event (wx.Event): The event triggered when pressing a key. If Esc is pressed, the dialog is closed;
			if Delete is pressed, the selected link is deleted; if F2 is pressed, the link is edited.
		"""

		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_F5:
			self.onToUpdate(event)
		elif keyCode == wx.WXK_DELETE:
			# Checks if focus is on an edit field
			focused = self.FindFocus()
			if isinstance(focused, (wx.TextCtrl, wx.SearchCtrl)):
				# Enables default Delete behavior
				event.Skip()
				return
			self.onDelete(event)
		elif keyCode == wx.WXK_F2:
			self.onEdit(event)
		event.Skip()

	def onClose(self, event):
		"""
		closes the window.

		Args:
			event (wx.Event): Event triggered by the cancel button.
		"""
		self.Destroy()
