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
from .varsConfig import ADDON_SUMMARY, ourAddon

# Initializes the translation
addonHandler.initTranslation()


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
		size = wx.Size(WIDTH, HEIGHT)
		try:
			self.contactResults = core.get_all_records()
		except EOFError:
			self.contactResults = []

		super(ContactList, self).__init__(
			parent, title=title, size=size, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

		# Creating the screen objects.
		panel = wx.Panel(self)
		self.contactList = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self.initialize_contact_list()

		# Selected line viewing field
		self.visualizationField = wx.TextCtrl(
			panel,
			style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_STATIC
		)

		# Translators: Search field label.
		labelSearch = wx.StaticText(panel, label=_("Search for: "))

		# List of combobox choices option.
		listOfOptions = [_("Name"), _("Cell phone"), _("Landline"), _("Email")]
		self.comboboxOptions = wx.ComboBox(panel, value=_("Name"), choices=listOfOptions)

		self.search = wx.SearchCtrl(panel, -1, size=wx.Size(250, 25))
		self.buttonSearch = wx.Button(panel, label=_("&Search"))

		# Vincula o evento de foco
		self.contactList.Bind(wx.EVT_SET_FOCUS, self.on_list_focus)

		# Selection event
		self.contactList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelectLine)

		# Define o foco na lista
		self.contactList.SetFocus()

		self.buttonNew = wx.Button(panel, wx.ID_NEW, label=_("&New"))
		self.buttonEdit = wx.Button(panel, wx.ID_EDIT, label=_("&Edit"))
		self.buttonDelete = wx.Button(panel, wx.ID_DELETE, label=_("&Remove"))
		self.buttonRefresh = wx.Button(panel, -1, label=_("Refres&h"))
		self.buttonImport = wx.Button(panel, -1, label=_("&Import csv..."))
		self.buttonExport = wx.Button(panel, -1, label=_("Ex&port csv..."))
		self.buttonResetRecords = wx.Button(panel, -1, label=_("&Delete all records."))
		self.buttonExit = wx.Button(panel, wx.ID_CANCEL, label=_("E&xit"))
		self.set_config()

		# Creating the layout and adding it to the panel.
		boxSizer = wx.BoxSizer(wx.VERTICAL)
		viewSizer = wx.BoxSizer(wx.VERTICAL)
		searchSizer = wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

		searchSizer.Add(labelSearch, 0, wx.ALL, 10)
		searchSizer.Add(self.comboboxOptions, 1, wx.ALL, 10)
		searchSizer.Add(self.search, 1, wx.ALL, 10)
		searchSizer.Add(self.buttonSearch, 0, wx.ALL, 10)
		viewSizer.Add(self.contactList, 1, wx.ALL | wx.EXPAND, 10)
		viewSizer.Add(self.visualizationField, 1, wx.ALL | wx.EXPAND, 10)

		buttonSizer.Add(self.buttonNew, 0, wx.ALL | wx.EXPAND, 5)
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

	def initialize_contact_list(self):
		"""Creating the columns of the ObjectListView."""
		self.contactList.ClearAll()
		columns = [
				(_("Name"), 250),
				(_("Cell phone"), 100),
				(_("Landline"), 100),
				(_("Email"), 300),
		]
		for i, (title, width) in enumerate(columns):
			self.contactList.InsertColumn(i, title, width=width)

		for record in self.contactResults:
			index = self.contactList.InsertItem(self.contactList.GetItemCount(), record.name)
			# Tupla com os atributos para um loop mais eficiente
			record_values = (
				record.cell,
				record.landline,
				record.email
			)
			for i, value in enumerate(record_values, start=1):
				self.contactList.SetItem(index, i, value)
			self.contactList.SetItemData(index, id(record))

	def onNew(self, event):
		"""Add a new record to the agenda."""
		dlg = AddEditRecDialog(gui.mainFrame)
		gui.mainFrame.prePopup()
		dlg.CentreOnScreen()
		dlg.ShowModal()
		dlg.Destroy()
		gui.mainFrame.postPopup()
		self._refresh_and_focus()

	def onEdit(self, event):
		"""Edit a selected record."""
		selectedRow = self.get_selected_record()
		if selectedRow is None:
			self.show_message(_("No records selected!"), _("Error"))
			return
		dlg = AddEditRecDialog(
			gui.mainFrame,
			selectedRow,
			title=_("To edit"),
			addRecord=False
		)
		gui.mainFrame.prePopup()
		dlg.CentreOnScreen()
		dlg.ShowModal()
		dlg.Destroy()
		gui.mainFrame.postPopup()
		self._refresh_and_focus()

	def onDelete(self, event):
		"""
		Deletes the selected record in the contact list after user confirmation.

		Args:
			event (wx.Event): The event that triggered this function.
		"""
		selectedRow = self.get_selected_record()
		if selectedRow is None:
			self.show_message(_("No records selected!"), _("Error"))
			return

		message = _("Do you want to delete the selected record?")
		caption = _("Attention")

		user_response = gui.messageBox(message, caption, style=wx.ICON_QUESTION | wx.YES_NO)
		if user_response == wx.YES:
			try:
				core.delete(selectedRow.id)
				self.show_message(_("Record deleted!"), _("Success"))
				self._refresh_and_focus()
			except Exception as e:
				self.show_message(_("Error deleting record: {}").format(str(e)), _("Error"))
				return
		self.contactList.SetFocus()

	def onSearch(self, event):
		"""Search using all the fields of the agenda."""
		# Gets the chosen filter option and the entered keyword
		filterChoice = self.comboboxOptions.GetValue()
		keyword = self.search.GetValue()

		if not keyword or keyword.strip() == "":
			self.show_message(_("The search field is empty!"), _("Attention"))
			self.search.SetFocus()
			return

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
				self.initialize_contact_list()

				# Clear the search field after searching
				self.search.Clear()

				# Sets focus back to the contact list for easier navigation
				self.contactList.SetFocus()
		except Exception as e:
			# Display an error message if an exception occurs during the search
			self.show_message("{}".format(e))

	def onToImport(self, event):
		"""Import csv file to the agenda."""
		dlg = wx.FileDialog(
			self, _("import csv file"),
			os.getcwd(), "", "*.csv", wx.FD_OPEN
		)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				mypath = dlg.GetPath()
				core.import_csv_to_db(mypath)
				self.show_message(_("File imported successfully!"), _("Attention"))
				self.contactList.SetFocus()
		except Exception as e:
			msg = _("""It was not possible to import the file! {}""".format(e))

			# Translators: Message displayed to the user in case of errors when importing the CSV file
			self.show_message(msg, _("Attention"))
		finally:
			dlg.Destroy()
		self._refresh_and_focus()

	def onToExport(self, event):
		"""Export the calendar to csv."""
		dlg = wx.FileDialog(
			self,
			_("export csv file"),
			os.getcwd(),
			"agenda",
			"*.csv",
			wx.FD_SAVE
		)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				mypath = dlg.GetPath()
				core.export_db_to_csv(mypath)
				self.show_message(_("File exported successfully!"), _("Attention"))
				self.contactList.SetFocus()
		except Exception as e:
			msg = _("""It was not possible to export the file! {}""").format(e)
			# Translators: Message displayed to the user in case of errors when exporting the CSV file
			self.show_message(msg, _("Attention"))
		finally:
			dlg.Destroy()
		self._refresh_and_focus()

	# Clear all the agenda.
	def onReset(self, event):
		"""
		Resets all phonebook records after user confirmation.

		Args:
			event (wx.Event): The event that triggered this function.
		"""

		# 1. Obtains the counting of records safely.
		record_count = core.count_records()

		# 2. Checks the three possible scenarios: failure, empty list or list with records.
		if record_count is None:
			# If Record Count for None, there was an error in the database.
			# The error message is already displayed internally by the Core.COUNT Records function.
			self.show_message(_("An error occurred while counting records. Check the logs."), _("Error"))
			return

		elif record_count == 0:
			# If Record Count for 0, the agenda is already empty.
			self.show_message(_("The agenda is already empty!"), _("Attention"))
			return

		# 3. If Record Count> 0, requests user confirmation.
		message = _("This operation erases all phonebook entries. Do you wish to continue?")
		caption = _("Attention")

		user_response = gui.messageBox(message, caption, style=wx.ICON_QUESTION | wx.YES_NO)
		if user_response == wx.YES:
			try:
				core.reset_record()
				self.show_message(_("Agenda deleted!"), _("Success"))
				self._refresh_and_focus()
			except Exception as e:
				self.show_message(_("Error deleting records: {}").format(str(e)), _("Error"))
				return

		# 4. Refreshes the list and sets focus, encapsulating repeated calls.
		self._refresh_and_focus()

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

	def get_selected_record(self):
		index = self.contactList.GetFirstSelected()
		if index == -1:
			return None
		itemId = self.contactList.GetItemData(index)
		for obj in self.contactResults:
			if id(obj) == itemId:
				return obj
		return None

	def onSelectLine(self, event):
		# Check if there is a line selected in the list
		selected_idx = self.contactList.GetFirstSelected()
		if selected_idx == -1:
			return

		data = [
			f"{self.contactList.GetColumn(i).GetText()}: {self.contactList.GetItem(selected_idx, i).GetText()}"
			for i in range(self.contactList.GetColumnCount())
		]
		lineComplete = " | ".join(data)
		self.visualizationField.SetValue(lineComplete)

	def show_all_records(self):
		self.contactResults = core.get_all_records()
		self.initialize_contact_list()

	def _refresh_and_focus(self):
		self.show_all_records()
		self.visualizationField.SetValue("")
		self.contactList.SetFocus()

	def onToUpdate(self, event):
		self._refresh_and_focus()
		ui.message(_("Updated records!"))

	def on_list_focus(self, event):
		if self.contactList.GetItemCount() > 0:
			self.contactList.SetItemState(0, wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED,
									  	wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED)
			self.contactList.EnsureVisible(0)
		if event is not None:
			event.Skip()
