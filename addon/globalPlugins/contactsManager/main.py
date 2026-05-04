# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 30/11/2022.
"""

import os
import re
import webbrowser

import addonHandler
import config
import gui
import queueHandler
import ui
import wx
from gui import guiHelper
from logHandler import log

from . import controller as core
from .addEditRecord import AddEditRecDialog
from .varsConfig import ADDON_SUMMARY, ourAddon

# Initialize translation support
addonHandler.initTranslation()


class ContactList(wx.Dialog):
	_instance = None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		if ContactList._instance is None:
			return super(ContactList, cls).__new__(cls, *args, **kwargs)
		return ContactList._instance

	def __init__(self, parent, title):
		if ContactList._instance is not None:
			return
		ContactList._instance = self

		self.title = title

		try:
			self.contactResults = core.getAllRecords()
		except EOFError:
			self.contactResults = []

		super(ContactList, self).__init__(parent, title=title,
			style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
			size=wx.Size(900, 450)
		)
		self.Bind(wx.EVT_WINDOW_DESTROY, self._onInternalDestroy)
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

		# WIDGETS
		panel = wx.Panel(self)
		self.contactList = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self.initializeContactList()

		self.visualizationField = wx.TextCtrl(
			panel,
			style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_STATIC
		)

		labelSearch = wx.StaticText(panel, label=_("Search for: "))
		listOfOptions = [_("Name"), _("Cell phone"), _("Landline"), _("Email")]
		self.comboboxOptions = wx.ComboBox(panel, value=_("Name"), choices=listOfOptions)

		self.search = wx.SearchCtrl(panel, -1, size=wx.Size(250, 25))
		self.buttonSearch = wx.Button(panel, label=_("&Search"))

		self.contactList.Bind(wx.EVT_SET_FOCUS, self.onListFocus)
		self.contactList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelectLine)
		self.contactList.SetFocus()

		# Buttons
		self.buttonNew = wx.Button(panel, wx.ID_NEW, label=_("&New"))
		self.buttonEdit = wx.Button(panel, wx.ID_EDIT, label=_("&Edit"))
		self.buttonWhatsApp = wx.Button(panel, -1, label=_("&WhatsApp"))
		self.buttonDelete = wx.Button(panel, wx.ID_DELETE, label=_("&Remove"))
		self.buttonRefresh = wx.Button(panel, -1, label=_("Refres&h"))
		self.buttonImport = wx.Button(panel, -1, label=_("&Import csv..."))
		self.buttonExport = wx.Button(panel, -1, label=_("Ex&port csv..."))
		self.buttonResetRecords = wx.Button(panel, -1, label=_("&Delete all records."))
		self.buttonExit = wx.Button(panel, wx.ID_CANCEL, label=_("E&xit"))

		self.set_config()

		# -------- LAYOUT --------
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

		buttonSizer.Add(self.buttonNew, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonEdit, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonWhatsApp, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonDelete, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonRefresh, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonImport, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonExport, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonResetRecords, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonExit, 0, wx.ALL, 5)

		boxSizer.Add(searchSizer, wx.ALL, guiHelper.BORDER_FOR_DIALOGS)
		boxSizer.Add(viewSizer, wx.ALL, guiHelper.BORDER_FOR_DIALOGS)
		boxSizer.Add(buttonSizer, 0, wx.CENTER)
		panel.SetSizerAndFit(boxSizer)
		self.Fit()

		# -------- EVENTS --------
		self.buttonSearch.Bind(wx.EVT_BUTTON, self.onSearch)
		self.buttonEdit.Bind(wx.EVT_BUTTON, self.onEdit)
		self.buttonNew.Bind(wx.EVT_BUTTON, self.onNew)
		self.buttonWhatsApp.Bind(wx.EVT_BUTTON, self.onWhatsApp)
		self.buttonDelete.Bind(wx.EVT_BUTTON, self.onDelete)
		self.buttonRefresh.Bind(wx.EVT_BUTTON, self.onToUpdate)
		self.buttonImport.Bind(wx.EVT_BUTTON, self.onToImport)
		self.buttonExport.Bind(wx.EVT_BUTTON, self.onToExport)
		self.buttonResetRecords.Bind(wx.EVT_BUTTON, self.onReset)
		self.buttonExit.Bind(wx.EVT_BUTTON, self.onClose)

	def initializeContactList(self):
		self.contactList.ClearAll()
		self._itemMap = {}  # SAFE ITEM MAP

		columns = [
			(_("Name"), 250),
			(_("Cell phone"), 100),
			(_("Landline"), 100),
			(_("Email"), 300),
		]
		for i, (title, width) in enumerate(columns):
			self.contactList.InsertColumn(i, title, width=width)

		for rowIndex, record in enumerate(self.contactResults):
			i = self.contactList.InsertItem(self.contactList.GetItemCount(), record.name)

			values = (record.cell, record.landline, record.email)
			for col, value in enumerate(values, start=1):
				self.contactList.SetItem(i, col, value)

			# SAVE THE OBJECT ON THE SECURE MAP
			self._itemMap[i] = record

			# SAVE THE INDEX IN LISTCTRL (only accepts integers!)
			self.contactList.SetItemData(i, i)

	def getSelectedRecord(self):
		index = self.contactList.GetFirstSelected()
		if index == -1:
			return None
		return self._itemMap.get(index) # SAFE RETURN

	def onNew(self, event):
		dlg = AddEditRecDialog(gui.mainFrame)
		gui.mainFrame.prePopup()
		dlg.ShowModal()
		gui.mainFrame.postPopup()
		self._refreshAndFocus()

	def onEdit(self, event):
		selected = self.getSelectedRecord()
		if not selected:
			self.showMessage(_("No records selected!"), _("Error"))
			return
		dlg = AddEditRecDialog(gui.mainFrame, selected, title=_("To edit"), addRecord=False)
		gui.mainFrame.prePopup()
		dlg.ShowModal()
		gui.mainFrame.postPopup()
		self._refreshAndFocus()

	def onWhatsApp(self, event):
		selected = self.getSelectedRecord()
		if not selected:
			# translators: Message shown when no record is selected
			self.showMessage(_("No records selected!"), _("Error"))
			return

		cleanNumber = re.sub(r'\D', '', selected.cell)

		if not cleanNumber:
			msg = _("The cell phone field for {} is empty.").format(selected.name)
			# translators: Message shown when a contact has an empty cell phone field
			ui.message(msg)
			return

		# Add country code to number
		countryCode = config.conf[ourAddon.name]["countryCode"]
		cleanNumber = countryCode   + cleanNumber

		# Usando o protocolo da aplicação em vez de HTTPS
		url = f"whatsapp://send?phone={cleanNumber}"
		log.warning(f"number formatted with URL: {url}")		
		try:
			# O sistema tentará abrir a App do WhatsApp diretamente
			webbrowser.open(url)
			# translators: Message shown when contacting a record via WhatsApp
			ui.message(_("Contacting {} via WhatsApp").format(selected.name))
		except Exception as e:
			# Caso o protocolo falhe, voltamos ao método do navegador como plano B
			urlFallback = f"https://wa.me/{cleanNumber}"
			log.warning(f"number formatted with URL Fall back: {urlFallback}")		
			webbrowser.open(urlFallback)

	def onDelete(self, event):
		selected = self.getSelectedRecord()
		if not selected:
			self.showMessage(_("No records selected!"), _("Error"))
			return
		if gui.messageBox(_("Do you want to delete the selected record?"),
						  _("Attention"),
						  wx.YES_NO) == wx.YES:
			core.delete(selected.id)
			self.showMessage(_("Record deleted!"))
			self._refreshAndFocus()

	def onSearch(self, event):
		filterChoice = self.comboboxOptions.GetValue()
		keyword = self.search.GetValue()

		if not keyword.strip():
			self.showMessage(_("The search field is empty!"), _("Attention"))
			self.search.SetFocus()
			return

		try:
			self.contactResults = core.searchRecords(filterChoice, keyword)
			if not self.contactResults:
				self.showMessage(_("No contacts found matching the search criteria."))
				self.search.SetFocus()
			else:
				self.initializeContactList()
				self.search.Clear()
				self.contactList.SetFocus()
		except Exception as e:
			self.showMessage(str(e))

	def onToImport(self, event):
		dlg = wx.FileDialog(self, _("import csv file"), os.getcwd(), "", "*.csv", wx.FD_OPEN)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				core.importCsvToDb(dlg.GetPath())
				self.showMessage(_("File imported successfully!"))
		finally:
			dlg.Destroy()
		self._refreshAndFocus()

	def onToExport(self, event):
		dlg = wx.FileDialog(self, _("export csv file"), os.getcwd(), "agenda",
							"*.csv", wx.FD_SAVE)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				core.exportDbToCsv(dlg.GetPath())
				self.showMessage(_("File exported successfully!"))
		finally:
			dlg.Destroy()
		self._refreshAndFocus()

	def onReset(self, event):
		count = core.countRecords()
		if count is None:
			self.showMessage(_("Error counting records."), _("Error"))
			return
		if count == 0:
			self.showMessage(_("The agenda is already empty!"))
			return
		if gui.messageBox(_("Erase ALL records?"), _("Attention"),
						  wx.YES_NO) == wx.YES:
			core.resetRecord()
			self.showMessage(_("Agenda deleted!"))
		self._refreshAndFocus()

	def set_config(self):
		if not config.conf[ourAddon.name]["resetRecords"]:
			self.buttonResetRecords.Disable()
		if (not config.conf[ourAddon.name]["importCSV"]) or (not config.conf[ourAddon.name]["exportCSV"]):
			self.buttonExport.Disable()
			self.buttonImport.Disable()

	def showMessage(self, message, caption=_("Message"),
					 style=wx.OK | wx.ICON_INFORMATION):
		gui.messageBox(message, caption, style)

	def onKeyPress(self, event):
		keyCode = event.GetKeyCode()
		focused = self.FindFocus() # Identifica onde o utilizador está

		if keyCode == wx.WXK_F5:
			self.onToUpdate(event)
		elif keyCode == wx.WXK_DELETE:
			if isinstance(focused, (wx.TextCtrl, wx.SearchCtrl)):
				event.Skip()
				return
			self.onDelete(event)
		elif keyCode == wx.WXK_F2:
			self.onEdit(event)
			event.Skip()
		elif keyCode == wx.WXK_RETURN:
			# If the focus is on the search, execute the search
			if focused == self.search:
				self.onSearch(event)
			# If the focus is on the list, open WhatsApp
			elif focused == self.contactList:
				self.onWhatsApp(event)
			else:
				event.Skip() # Allows default behavior in other fields
				return
		event.Skip()

	def showMessage(self, message, caption=None, style=wx.OK | wx.ICON_INFORMATION):
		"""
		Displays a message to the user in a dialog box.
		"""

		if caption is None:
			# translators: Title of message dialog box.
			caption = _("Attention")

		gui.messageBox(message, caption, style)

	def onClose(self, event):
		self.Destroy()

	def onSelectLine(self, event):
		idx = self.contactList.GetFirstSelected()
		if idx == -1:
			return
		data = [
			f"{self.contactList.GetColumn(i).GetText()}: {self.contactList.GetItemText(idx, i)}"
			for i in range(self.contactList.GetColumnCount())
		]
		self.visualizationField.SetValue(" | ".join(data))

	def showAllRecords(self):
		self.contactResults = core.getAllRecords()
		self.initializeContactList()

	def _refreshAndFocus(self):
		self.showAllRecords()
		self.visualizationField.SetValue("")
		self.contactList.SetFocus()

	def onToUpdate(self, event):
		self._refreshAndFocus()
		ui.message(_("Updated records!"))

	def onListFocus(self, event):
		if self.contactList.GetItemCount() > 0:
			self.contactList.SetItemState(0,
				wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED,
				wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED
			)
			self.contactList.EnsureVisible(0)
		event.Skip()

	def _onInternalDestroy(self, event):
		# Clears the Singleton instance so that the next __new__ creates a new one
		ContactList._instance = None
		event.Skip()
 