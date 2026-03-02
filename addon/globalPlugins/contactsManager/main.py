# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 30/11/2022
"""

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

# Initialize translation support
addonHandler.initTranslation()


class ContactList(wx.Dialog):
	"""
	Contact list dialog for the contacts add-on.
	"""

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
		self._sort_column = 0
		self._sort_ascending = True

		try:
			self.contactResults = core.get_all_records()
		except EOFError:
			self.contactResults = []

		super(ContactList, self).__init__(
			parent,
			title=title,
			style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
			size=wx.Size(900, 450),
		)

		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

		# Widgets
		panel = wx.Panel(self)
		self.contactList = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self._itemMap = {}
		self.initialize_contact_list()

		self.visualizationField = wx.TextCtrl(
			panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_STATIC
		)

		label_search = wx.StaticText(panel, label=_("Search for: "))
		choices = [_("Name"), _("Cell phone"), _("Landline"), _("Email")]
		self.comboboxOptions = wx.Choice(panel, choices=choices)
		self.comboboxOptions.SetSelection(0)

		self.search = wx.SearchCtrl(panel, -1, size=wx.Size(250, 25))
		self.buttonSearch = wx.Button(panel, label=_("&Search"))

		# Buttons (keep references for set_config)
		self.buttonNew = wx.Button(panel, wx.ID_NEW, label=_("&New"))
		self.buttonEdit = wx.Button(panel, wx.ID_EDIT, label=_("&Edit"))
		self.buttonDelete = wx.Button(panel, wx.ID_DELETE, label=_("&Remove"))
		self.buttonImport = wx.Button(panel, -1, label=_("&Import csv..."))
		self.buttonExport = wx.Button(panel, -1, label=_("Ex&port csv..."))
		self.buttonResetRecords = wx.Button(panel, -1, label=_("&Delete all records."))
		self.buttonRefresh = wx.Button(panel, -1, label=_("Refres&h"))
		self.buttonExit = wx.Button(panel, wx.ID_CANCEL, label=_("E&xit"))

		self.set_config()

		# Layout
		box_sizer = wx.BoxSizer(wx.VERTICAL)
		view_sizer = wx.BoxSizer(wx.VERTICAL)
		search_sizer = wx.BoxSizer(wx.HORIZONTAL)
		button_sizer = wx.BoxSizer(wx.HORIZONTAL)

		search_sizer.Add(label_search, 0, wx.ALL, 10)
		search_sizer.Add(self.comboboxOptions, 0, wx.ALL, 10)
		search_sizer.Add(self.search, 1, wx.ALL, 10)
		search_sizer.Add(self.buttonSearch, 0, wx.ALL, 10)

		view_sizer.Add(self.contactList, 1, wx.ALL | wx.EXPAND, 10)
		view_sizer.Add(self.visualizationField, 1, wx.ALL | wx.EXPAND, 10)

		for b in [
			self.buttonNew, self.buttonEdit, self.buttonDelete,
			self.buttonImport, self.buttonExport, self.buttonResetRecords,
			self.buttonRefresh, self.buttonExit
		]:
			button_sizer.Add(b, 0, wx.ALL | wx.EXPAND, 5)

		box_sizer.Add(search_sizer, wx.ALL, guiHelper.BORDER_FOR_DIALOGS)
		box_sizer.Add(view_sizer, wx.ALL, guiHelper.BORDER_FOR_DIALOGS)
		box_sizer.Add(button_sizer, 0, wx.CENTER)
		panel.SetSizerAndFit(box_sizer)
		self.Fit()

		# Events
		self.buttonSearch.Bind(wx.EVT_BUTTON, self.onSearch)
		self.buttonNew.Bind(wx.EVT_BUTTON, self.onNew)
		self.buttonEdit.Bind(wx.EVT_BUTTON, self.onEdit)
		self.buttonDelete.Bind(wx.EVT_BUTTON, self.onDelete)
		self.buttonImport.Bind(wx.EVT_BUTTON, self.onToImport)
		self.buttonExport.Bind(wx.EVT_BUTTON, self.onToExport)
		self.buttonResetRecords.Bind(wx.EVT_BUTTON, self.onReset)
		self.buttonRefresh.Bind(wx.EVT_BUTTON, self.onToUpdate)
		self.buttonExit.Bind(wx.EVT_BUTTON, self.onClose)

		# List events
		self.contactList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelectLine)
		self.contactList.Bind(wx.EVT_LIST_COL_CLICK, self.on_column_click)
		self.contactList.Bind(wx.EVT_SET_FOCUS, self.on_list_focus)

		# allow Enter in search to trigger search
		self.search.Bind(wx.EVT_TEXT_ENTER, self.onSearch)
		self.contactList.SetFocus()

	# List population and mapping
	def initialize_contact_list(self, preserve_selected_id=None):
		"""Populate the list from self.contactResults. Optionally restore selection by record id."""
		self.contactList.ClearAll()
		self._itemMap = {}

		columns = [
			(_("Name"), 250),
			(_("Cell phone"), 100),
			(_("Landline"), 100),
			(_("Email"), 300),
		]
		for col_idx, (title, width) in enumerate(columns):
			self.contactList.InsertColumn(col_idx, title, width=width)

		selected_index = None
		for record in self.contactResults:
			i = self.contactList.InsertItem(self.contactList.GetItemCount(), record.name or "")

			values = (record.cell or "", record.landline or "", record.email or "")
			for col, value in enumerate(values, start=1):
				self.contactList.SetItem(i, col, value)

			self._itemMap[i] = record
			# store index as item data (wx.ListCtrl accepts ints)
			self.contactList.SetItemData(i, i)

			if preserve_selected_id is not None and getattr(record, "id", None) == preserve_selected_id:
				selected_index = i

		if selected_index is not None:
			self.contactList.Select(selected_index)
			self.contactList.Focus(selected_index)
			self.contactList.EnsureVisible(selected_index)

	def _get_selected_id(self):
		"""Return id of currently selected record (or None)."""
		selected = self.get_selected_record()
		return getattr(selected, "id", None) if selected is not None else None

	def get_selected_record(self):
		idx = self.contactList.GetFirstSelected()
		if idx == -1:
			return None
		return self._itemMap.get(idx)

	# Sorting
	_COLUMN_ATTR_MAP = {
		0: "name",
		1: "cell",
		2: "landline",
		3: "email",
	}

	def on_column_click(self, event):
		col = event.GetColumn()
		if col not in self._COLUMN_ATTR_MAP:
			return
		if self._sort_column == col:
			self._sort_ascending = not self._sort_ascending
		else:
			self._sort_column = col
			self._sort_ascending = True

		attr = self._COLUMN_ATTR_MAP[col]
		selected_id = self._get_selected_id()

		def _key(r):
			v = getattr(r, attr, "")
			if v is None:
				return ""
			if isinstance(v, str):
				return v.lower()
			try:
				return str(v).lower()
			except Exception:
				return ""

		self.contactResults.sort(key=_key, reverse=not self._sort_ascending)
		self.initialize_contact_list(preserve_selected_id=selected_id)

	# Actions
	def onNew(self, event):
		dlg = AddEditRecDialog(gui.mainFrame)
		gui.mainFrame.prePopup()
		dlg.CentreOnScreen()
		dlg.ShowModal()
		dlg.Destroy()
		gui.mainFrame.postPopup()
		self._refresh_and_focus()

	def onEdit(self, event):
		selected = self.get_selected_record()
		if not selected:
			self.show_message(_("No records selected!"), _("Error"))
			return
		dlg = AddEditRecDialog(gui.mainFrame, selected, title=_("To edit"), addRecord=False)
		gui.mainFrame.prePopup()
		dlg.CentreOnScreen()
		dlg.ShowModal()
		dlg.Destroy()
		gui.mainFrame.postPopup()
		self._refresh_and_focus()

	def onDelete(self, event):
		selected = self.get_selected_record()
		if not selected:
			self.show_message(_("No records selected!"), _("Error"))
			return
		message = _("Do you want to delete the selected record?")
		if gui.messageBox(message, _("Attention"), wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
			try:
				core.delete(selected.id)
				self.show_message(_("Record deleted!"))
			except Exception as exc:
				self.show_message(_("Error deleting record: {}").format(str(exc)), _("Error"))
				return
			self._refresh_and_focus()
		self.contactList.SetFocus()

	def onSearch(self, event):
		filter_choice = self.comboboxOptions.GetStringSelection()
		keyword = self.search.GetValue()
		if not keyword or not keyword.strip():
			self.show_message(_("The search field is empty!"), _("Attention"))
			self.search.SetFocus()
			return

		try:
			selected_id = self._get_selected_id()
			self.contactResults = core.search_records(filter_choice, keyword)
			if not self.contactResults:
				self.show_message(_("No contacts found matching the search criteria."))
				self.search.SetFocus()
			else:
				self.initialize_contact_list(preserve_selected_id=selected_id)
				self.search.Clear()
				self.contactList.SetFocus()
		except Exception as exc:
			self.show_message(str(exc), _("Error"))

	def onToImport(self, event):
		with wx.FileDialog(self, _("import csv file"), os.getcwd(), "", "*.csv", wx.FD_OPEN) as dlg:
			if dlg.ShowModal() == wx.ID_OK:
				try:
					core.import_csv_to_db(dlg.GetPath())
					self.show_message(_("File imported successfully!"), _("Attention"))
				except Exception as exc:
					self.show_message(_("It was not possible to import the file! {}").format(str(exc)), _("Attention"))
		self._refresh_and_focus()

	def onToExport(self, event):
		with wx.FileDialog(self, _("export csv file"), os.getcwd(), "agenda", "*.csv", wx.FD_SAVE) as dlg:
			if dlg.ShowModal() == wx.ID_OK:
				try:
					core.export_db_to_csv(dlg.GetPath())
					self.show_message(_("File exported successfully!"), _("Attention"))
				except Exception as exc:
					self.show_message(_("It was not possible to export the file! {}").format(str(exc)), _("Attention"))
		self._refresh_and_focus()

	def onReset(self, event):
		count = core.count_records()
		if count is None:
			self.show_message(_("Error counting records."), _("Error"))
			return
		if count == 0:
			self.show_message(_("The agenda is already empty!"))
			return
		if gui.messageBox(_("This operation erases all phonebook entries. Do you wish to continue?"),
						  _("Attention"), wx.ICON_QUESTION | wx.YES_NO) == wx.YES:
			try:
				core.reset_record()
				self.show_message(_("Agenda deleted!"))
			except Exception as exc:
				self.show_message(_("Error deleting records: {}").format(str(exc)), _("Error"))
		self._refresh_and_focus()

	def set_config(self):
		if not config.conf[ourAddon.name]["resetRecords"]:
			self.buttonResetRecords.Disable()
		if (not config.conf[ourAddon.name]["importCSV"]) or (not config.conf[ourAddon.name]["exportCSV"]):
			self.buttonExport.Disable()
			self.buttonImport.Disable()

	def show_message(self, message, caption=_("Message"), style=wx.OK | wx.ICON_INFORMATION):
		gui.messageBox(message, caption, style)

	def onKeyPress(self, event):
		key_code = event.GetKeyCode()
		if event.ControlDown() and key_code in (ord("n"), ord("N")):
			self.onNew(event)
			return
		if key_code in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			focused = self.FindFocus()
			if focused is self.contactList or isinstance(focused, wx.ListCtrl):
				self.onEdit(event)
				return
		if key_code == wx.WXK_F5:
			self.onToUpdate(event)
			return
		if key_code == wx.WXK_DELETE:
			focused = self.FindFocus()
			if isinstance(focused, (wx.TextCtrl, wx.SearchCtrl)):
				event.Skip()
				return
			self.onDelete(event)
			return
		if key_code == wx.WXK_F2:
			self.onEdit(event)
			return
		event.Skip()

	def onClose(self, event):
		self.Destroy()

	def show_all_records(self):
		self.contactResults = core.get_all_records()
		selected_id = self._get_selected_id()
		self.initialize_contact_list(preserve_selected_id=selected_id)

	def _refresh_and_focus(self):
		self.show_all_records()
		self.visualizationField.SetValue("")
		self.contactList.SetFocus()

	def onToUpdate(self, event):
		self._refresh_and_focus()
		ui.message(_("Updated records!"))

	def on_list_focus(self, event):
		if self.contactList.GetItemCount() > 0:
			self.contactList.SetItemState(
				0,
				wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED,
				wx.LIST_STATE_SELECTED | wx.LIST_STATE_FOCUSED,
			)
			self.contactList.EnsureVisible(0)
		event.Skip()

	def onSelectLine(self, event):
		idx = self.contactList.GetFirstSelected()
		if idx == -1:
			return
		data = [
			f"{self.contactList.GetColumn(i).GetText()}: {self.contactList.GetItemText(idx, i)}"
			for i in range(self.contactList.GetColumnCount())
		]
		self.visualizationField.SetValue(" | ".join(data))
