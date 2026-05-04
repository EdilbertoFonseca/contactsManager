# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 - 2026 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

-------------------------------------------------------------------------
AI DISCLOSURE / NOTA DE IA:
This project utilizes AI for code refactoring and logic suggestions.
All AI-generated code was manually reviewed and tested by the author.
-------------------------------------------------------------------------

Created on: 30/11/2022.
"""

import os
import re
import sys

import addonHandler
import config
import gui
import wx
from logHandler import log

from . import controller as core
from .varsConfig import ADDON_PATH, EMAIL_REGEX, IS64, ourAddon

# Add the lib/ folder to sys.path (only once)
libFolder = "lib64" if IS64 else "lib"
libPath = os.path.join(ADDON_PATH, libFolder)

if os.path.isdir(libPath) and libPath not in sys.path:
	sys.path.insert(0, libPath)

try:
	from masked.textctrl import TextCtrl
except ImportError as e:
	log.error(f"[{ADDON_NAME}] Error when importing internal library 'masked': {e}")
	raise ImportError(_("Mandatory Library Absent: Masked"))

# Initialize translation support
addonHandler.initTranslation()

def validateFields(data):
	"""
	Validates the fields of the contact form.

	Args:
		data (dict): Data from the form to be validated.

	Returns:
		dict: A dictionary of errors with the invalid fields and their respective messages.
	"""

	errors = {}

	# Validation of mandatory fields is essential to avoid corrupted data.
	if not data.get("name"):
		errors["name"] = _("It is necessary to inform the name!")
	if not data.get("landline"):
		errors["landline"] = _("It is necessary to inform the landline!")
	# Email validation is done only if the field is not empty.
	if data.get("email") and not re.match(EMAIL_REGEX, data["email"]):
		errors["email"] = _("Invalid email format!")

	return errors


class AddEditRecDialog(wx.Dialog):

	def __init__(self, parent, row=None, title=_("Add"), addRecord=True):
		# Dialog window title.
		self.title = title
		WIDTH = 600
		HEIGHT = 300

		wx.Dialog.__init__(
			self, parent, title=_("{} Record in Contacts Manager for NVDA").format(title), size=(WIDTH, HEIGHT))

		# Check and apply settings.
		self.formatCellPhone = config.conf[ourAddon.name]["formatCellPhone"]
		self.formatLandline = config.conf[ourAddon.name]["formatLandline"]

		self.addRecord = addRecord  # Defines whether it is a new record or an edit
		self.selectedRow = row  # Stores the selected line, if any

		# Simplified initialization of variables.
		name = self.selectedRow.name if self.selectedRow else ""
		cell = self.selectedRow.cell if self.selectedRow else ""
		landline = self.selectedRow.landline if self.selectedRow else ""
		email = self.selectedRow.email if self.selectedRow else ""

		# Creating the widgets.
		self.panel = wx.Panel(self)
		labelName = wx.StaticText(self.panel, label=_("Name: "))
		self.textName = wx.TextCtrl(self.panel, -1, value=name, size=(200, 25), style=wx.TE_PROCESS_ENTER)

		labelCell = wx.StaticText(self.panel, label=_("Cell phone: "))
		self.textCell = TextCtrl(self.panel, value=cell, mask=self.formatCellPhone, style=wx.TE_PROCESS_ENTER)

		labelLandline = wx.StaticText(self.panel, label=_("Landline: "))
		self.textLandline = TextCtrl(
			self.panel, value=landline, mask=self.formatLandline, style=wx.TE_PROCESS_ENTER)

		labelEmail = wx.StaticText(self.panel, label=_("Email: "))
		self.textEmail = wx.TextCtrl(self.panel, value=email, size=(200, 25), style=wx.TE_PROCESS_ENTER)

		self.buttonOk = wx.Button(self.panel, wx.ID_OK, label=_("&Ok"))
		self.buttonOk.Bind(wx.EVT_BUTTON, self.handleRecord)

		self.buttonCancel = wx.Button(self.panel, wx.ID_CANCEL, label=_("&Cancel"))
		self.buttonCancel.Bind(wx.EVT_BUTTON, self.onClose)

		# Creating the screen objects.
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		viewSizer = wx.BoxSizer(wx.VERTICAL)
		viewSizer.Add(labelName, 0, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(self.textName, 1, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(labelCell, 0, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(self.textCell, 0, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(labelLandline, 0, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(self.textLandline, 0, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(labelEmail, 0, wx.ALL | wx.EXPAND, 5)
		viewSizer.Add(self.textEmail, 0, wx.ALL | wx.EXPAND, 5)

		buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
		buttonSizer.Add(self.buttonOk, 0, wx.ALL, 5)
		buttonSizer.Add(self.buttonCancel, 0, wx.ALL, 5)

		mainSizer.Add(viewSizer, wx.EXPAND)
		mainSizer.Add(buttonSizer, 0, wx.CENTER)
		self.panel.SetSizerAndFit(mainSizer)

		# Binding EVT_TEXT_ENTER events to corresponding methods
		self.textCell.Bind(wx.EVT_CHAR_HOOK, self.onPasteAndClean)
		self.textLandline.Bind(wx.EVT_CHAR_HOOK, self.onPasteAndClean)
		self.textName.Bind(wx.EVT_TEXT_ENTER, self.onFocusName)
		self.textCell.Bind(wx.EVT_TEXT_ENTER, self.onFocusCell)
		self.textLandline.Bind(wx.EVT_TEXT_ENTER, self.onFocusLandline)
		self.textEmail.Bind(wx.EVT_TEXT_ENTER, self.onFocusEmail)

	def onFocusName(self, event):
		"""
		Focuses on the cell phone field when the name field is filled in.

		Args:
			event (wx.Event): The event generated by user interaction, usually a focus event.
		"""
		self.textCell.SetFocus()

	def onFocusCell(self, event):
		"""
		Focuses on the landline field when the cell phone field is filled in.

Args:
			event (wx.Event): The event generated by user interaction, usually a focus event.

		"""
		self.textLandline.SetFocus()

	def onFocusLandline(self, event):
		"""
		Focuses on the email field when the landline field is filled in.

		Args:
			event (wx.Event): The event generated by user interaction, usually a focus event.
		"""
		self.textEmail.SetFocus()

	def onFocusEmail(self, event):
		"""
		Focuses on the ok button when the email field is filled in.

		Args:
			event (wx.Event): The event generated by user interaction, usually a focus event.
		"""
		self.buttonOk.SetFocus()

	def getData(self):
		"""
		Collects and validates contact form data and returns it in a dictionary.

		Returns:
			dict or None: A dictionary with the contact's data if all fields are filled in and valid, or None if there
			are validation errors.
		"""

		# Form data collection
		contactDict = {
			"name": self.textName.GetValue().strip(),
			"cell": self.textCell.GetValue().strip(),
			"landline": self.textLandline.GetValue().strip(),
			"email": self.textEmail.GetValue().strip()
		}

		errors = validateFields(contactDict)
		if errors:
			# Take the first error and display the message
			field, message = next(iter(errors.items()))
			self.showMessage(message, _("Error"))
			self.focusField(field)
			return None

		return contactDict

	def onAdd(self):
		"""
		Adds a new contact to the database and displays a message to the user.

		This method collects the form data, adds the contact to the database, and presents a dialog box for the
		user to confirm whether they want to add a new contact or close the window.

		If there is an error adding the contact, an error message is displayed.

		Returns:
			None
		"""

		contactDict = self.getData()
		if not contactDict:
			return

		data = {"contacts": contactDict}
		success, error = self.saveContactToDb(data)

		if success:
			message = _("Contact added, want to add a new contact?")
			caption = _("Success")
			user_response = gui.messageBox(message, caption, style=wx.ICON_QUESTION | wx.YES_NO)
			if user_response == wx.YES:
				self.clearForm()
			else:
				self.Destroy()
		else:
			self.showMessage(_("Error adding contact: {}").format(error), _("Error"), wx.ICON_ERROR)

	def saveContactToDb(self, data):
		"""
		Save a contact in the database.

		Args:
			data (dict): Contact data to be saved.

		Returns:
			tuple: A boolean indicating success or failure, and an error message in case of failure.
		"""
		try:
			core.addRecord(data)
			return True, None
		except Exception as e:
			return False, str(e)

	def focusField(self, fieldName):
		"""
		Defines the focus on the field corresponding to the name of the provided field.

		Args:
			field_name (str): Name of the field to be focused.
		"""
		focusMapping = {
			"name": self.textName,
			"cell": self.textCell,
			"landline": self.textLandline,
			"email": self.textEmail,
		}
		if fieldName in focusMapping:
			focusMapping[fieldName].SetFocus()

	def onEdit(self):
		"""
		Edits the selected contact in the database and displays a success message to the user.
		"""
		contactDict = self.getData()
		if not contactDict:
			return

		try:
			core.editRecord(self.selectedRow.id, contactDict)
			self.showMessage(_("Contact edited!"), _("Success"), wx.ICON_INFORMATION)
			self.Destroy()
		except Exception as e:
			self.showMessage(_("Error editing contact: {}").format(str(e)), _("Error"), wx.ICON_ERROR)

	def handleRecord(self, event:wx.Event):
		"""
		Adds or edits a contact based on the form's current state.
		"""
		if self.addRecord:
			self.onAdd()
		else:
			self.onEdit()

	def clearForm(self):
		"""
		Cleans the fields of the form and position the focus on the first field.
		"""
		# Cleaning of safer and direct fields
		self.textName.SetValue("")
		self.textCell.SetValue("")
		self.textLandline.SetValue("")
		self.textEmail.SetValue("")
		self.textName.SetFocus()

	def showMessage(self, message, caption=None, style=wx.OK | wx.ICON_INFORMATION):
		"""
		Displays a message to the user in a dialog box.
		"""

		if caption is None:
			# translators: Title of message dialog box.
			caption = _("Attention")

		gui.messageBox(message, caption, style)

	# Cancels the dialog.
	def onClose(self, event:wx.Event):
		"""
		closes the window.

		Args:
			event (wx.Event): Event triggered by the cancel button.
		"""
		self.Destroy()

	def onPasteAndClean(self, event:wx.KeyEvent):
		"""
		Handles the Ctrl+V event, cleans the clipboard data, and intelligently
		aligns the numbers based on the current field's mask.
		"""
		# Check if the key combination is Ctrl+V
		if event.GetKeyCode() == ord("V") and event.ControlDown():
			# Get the currently focused field
			currentField = event.GetEventObject()

			# Open the system clipboard
			if not wx.TheClipboard.IsOpened():
				wx.TheClipboard.Open()
				dataObject = wx.TextDataObject()
				success = wx.TheClipboard.GetData(dataObject)
				wx.TheClipboard.Close()

				if success:
					rawText = dataObject.GetText()
					# 1. Clean the text: keep only digits
					cleanText = re.sub(r"\D", "", rawText)

					# 2. Identify the field's current mask
					currentMask = currentField.GetMask()

					# 3. Count how many digits (#) the mask supports
					maskDigitCount = currentMask.count("#")
					pastedDigitCount = len(cleanText)

					# 4. Automatic Alignment (Padding)
					# If the pasted string is shorter than the mask, we pad it with
					# leading spaces to prevent the mask from deleting initial digits.
					if 0 < pastedDigitCount < maskDigitCount:
						digitDifference = maskDigitCount - pastedDigitCount
						# Add leading spaces equivalent to the difference
						cleanText = (" " * digitDifference) + cleanText

					# 5. Set the formatted value into the field
					currentField.SetValue(cleanText)

					# 6. Intelligent Cursor Positioning
					# If the area was partially filled (e.g., missing Area Code),
					# we set the cursor to the beginning of the field.
					if pastedDigitCount < maskDigitCount:
						# Find the first editable position (the first #)
						firstEditablePos = currentMask.find("#")
						currentField.SetInsertionPoint(max(0, firstEditablePos))

					return  # Block the default system Paste action

		# If it's not Ctrl+V or success failed, let the event propagate
		event.Skip()
