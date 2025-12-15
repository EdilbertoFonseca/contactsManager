# -*- coding: UTF-8 -*-

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

		self.title = title

		try:
			self.contactResults = core.get_all_records()
		except EOFError:
			self.contactResults = []

		super(ContactList, self).__init__(parent, title=title,
			style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
			size=wx.Size(900, 450)
		)

		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

		# -------- UI --------
		panel = wx.Panel(self)
		self.contactList = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self.initialize_contact_list()

		self.visualizationField = wx.TextCtrl(
			panel,
			style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_STATIC
		)

		labelSearch = wx.StaticText(panel, label=_("Search for: "))
		listOfOptions = [_("Name"), _("Cell phone"), _("Landline"), _("Email")]
		self.comboboxOptions = wx.ComboBox(panel, value=_("Name"), choices=listOfOptions)

		self.search = wx.SearchCtrl(panel, -1, size=wx.Size(250, 25))
		self.buttonSearch = wx.Button(panel, label=_("&Search"))

		self.contactList.Bind(wx.EVT_SET_FOCUS, self.on_list_focus)
		self.contactList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelectLine)
		self.contactList.SetFocus()

		# Buttons
		self.buttonNew = wx.Button(panel, wx.ID_NEW, label=_("&New"))
		self.buttonEdit = wx.Button(panel, wx.ID_EDIT, label=_("&Edit"))
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
		self.buttonDelete.Bind(wx.EVT_BUTTON, self.onDelete)
		self.buttonRefresh.Bind(wx.EVT_BUTTON, self.onToUpdate)
		self.buttonImport.Bind(wx.EVT_BUTTON, self.onToImport)
		self.buttonExport.Bind(wx.EVT_BUTTON, self.onToExport)
		self.buttonResetRecords.Bind(wx.EVT_BUTTON, self.onReset)
		self.buttonExit.Bind(wx.EVT_BUTTON, self.onClose)


	# ============================================================
	# CORREÇÃO FUNDAMENTAL: MAPEAMENTO SEGURO DE OBJETOS
	# ============================================================
	def initialize_contact_list(self):
		self.contactList.ClearAll()
		self._itemMap = {}  # <======== NOVO (correção essencial)

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

			# GUARDA O OBJETO NO MAPA SEGURO
			self._itemMap[i] = record

			# GUARDA O ÍNDICE NO LISTCTRL (só aceita inteiros!)
			self.contactList.SetItemData(i, i)

	# ============================================================

	def get_selected_record(self):
		index = self.contactList.GetFirstSelected()
		if index == -1:
			return None
		return self._itemMap.get(index)  # <===== 100% correto no NVDA

	# ============================================================

	def onNew(self, event):
		dlg = AddEditRecDialog(gui.mainFrame)
		gui.mainFrame.prePopup()
		dlg.ShowModal()
		gui.mainFrame.postPopup()
		self._refresh_and_focus()

	def onEdit(self, event):
		selected = self.get_selected_record()
		if not selected:
			self.show_message(_("No records selected!"), _("Error"))
			return
		dlg = AddEditRecDialog(gui.mainFrame, selected, title=_("To edit"), addRecord=False)
		gui.mainFrame.prePopup()
		dlg.ShowModal()
		gui.mainFrame.postPopup()
		self._refresh_and_focus()

	def onDelete(self, event):
		selected = self.get_selected_record()
		if not selected:
			self.show_message(_("No records selected!"), _("Error"))
			return
		if gui.messageBox(_("Do you want to delete the selected record?"),
						  _("Attention"),
						  wx.YES_NO) == wx.YES:
			core.delete(selected.id)
			self.show_message(_("Record deleted!"))
			self._refresh_and_focus()

	def onSearch(self, event):
		filterChoice = self.comboboxOptions.GetValue()
		keyword = self.search.GetValue()

		if not keyword.strip():
			self.show_message(_("The search field is empty!"), _("Attention"))
			self.search.SetFocus()
			return

		try:
			self.contactResults = core.search_records(filterChoice, keyword)
			if not self.contactResults:
				self.show_message(_("No contacts found matching the search criteria."))
				self.search.SetFocus()
			else:
				self.initialize_contact_list()
				self.search.Clear()
				self.contactList.SetFocus()
		except Exception as e:
			self.show_message(str(e))

	def onToImport(self, event):
		dlg = wx.FileDialog(self, _("import csv file"), os.getcwd(), "", "*.csv", wx.FD_OPEN)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				core.import_csv_to_db(dlg.GetPath())
				self.show_message(_("File imported successfully!"))
		finally:
			dlg.Destroy()
		self._refresh_and_focus()

	def onToExport(self, event):
		dlg = wx.FileDialog(self, _("export csv file"), os.getcwd(), "agenda",
							"*.csv", wx.FD_SAVE)
		try:
			if dlg.ShowModal() == wx.ID_OK:
				core.export_db_to_csv(dlg.GetPath())
				self.show_message(_("File exported successfully!"))
		finally:
			dlg.Destroy()
		self._refresh_and_focus()

	def onReset(self, event):
		count = core.count_records()
		if count is None:
			self.show_message(_("Error counting records."), _("Error"))
			return
		if count == 0:
			self.show_message(_("The agenda is already empty!"))
			return
		if gui.messageBox(_("Erase ALL records?"), _("Attention"),
						  wx.YES_NO) == wx.YES:
			core.reset_record()
			self.show_message(_("Agenda deleted!"))
		self._refresh_and_focus()

	def set_config(self):
		if not config.conf[ourAddon.name]["resetRecords"]:
			self.buttonResetRecords.Disable()
		if (not config.conf[ourAddon.name]["importCSV"]) or (not config.conf[ourAddon.name]["exportCSV"]):
			self.buttonExport.Disable()
			self.buttonImport.Disable()

	def show_message(self, message, caption=_("Message"),
					 style=wx.OK | wx.ICON_INFORMATION):
		gui.messageBox(message, caption, style)

	def onKeyPress(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == wx.WXK_F5:
			self.onToUpdate(event)
		elif keyCode == wx.WXK_DELETE:
			focused = self.FindFocus()
			if isinstance(focused, (wx.TextCtrl, wx.SearchCtrl)):
				event.Skip()
				return
			self.onDelete(event)
		elif keyCode == wx.WXK_F2:
			self.onEdit(event)
		event.Skip()

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
			self.contactList.SetItemState(0,
				wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED,
				wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED
			)
			self.contactList.EnsureVisible(0)
		event.Skip()
