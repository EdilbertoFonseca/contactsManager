# -*- coding: UTF-8 -*-

# Description: Dialog box for adding and editing records in Contacts Manager for NVDA.
# Author: Edilberto Fonseca.
# Email: edilberto.fonseca@outlook.com
# Date of creation: 30/11/2022.

# Imports necessary for the add-on to function.
import logging
import os
import re
import sys

import addonHandler
import config
import gui
import wx

from . import controller as core
from .varsConfig import ourAddon

# Get a logger with the name of the current module
logger = logging.getLogger(__name__)

# Add directories to sys.path before importing libraries
baseDir = os.path.dirname(__file__)
libs = os.path.join(baseDir, "lib")
sys.path.append(libs)
try:
	from masked import TextCtrl
except Exception as e:
	logger.error(f"Error importing module: {str(e)}")

# For translation process
addonHandler.initTranslation()


class AddEditRecDialog(wx.Dialog):

	def __init__(self, parent, row=None, title=_('Add'), addRecord=True):
		# Dialog window title.
		self.title = title
		WIDTH = 600
		HEIGHT = 300

		wx.Dialog.__init__(
			self, parent, title=_('{} Record in Contacts Manager for NVDA').format(title), size=(WIDTH, HEIGHT))
		# Check and apply settings.
		self.formatCellPhone = config.conf[ourAddon.name]["formatCellPhone"]
		self.formatLandline = config.conf[ourAddon.name]["formatLandline"]

		self.addRecord = addRecord  # Defines whether it is a new record or an edit
		self.selectedRow = row  # Stores the selected line, if any

		name = cell = landline = email = ""  # Initialize the variables

		# If a line is selected, fill in the fields with the corresponding values
		if row:
			name = self.selectedRow.name
			cell = self.selectedRow.cell
			landline = self.selectedRow.landline
			email = self.selectedRow.email
		else:
			if name is None or cell is None or landline is None or email is None:
				# Initialize variables as empty strings if the selected line does not exist
				name = cell = landline = email = ""

		# Creating the widgets.
		self.panel = wx.Panel(self)
		labelName = wx.StaticText(self.panel, label=_('Name: '))
		self.textName = wx.TextCtrl(self.panel, -1, value=name, size=(200, 25), style=wx.TE_PROCESS_ENTER)

		labelCell = wx.StaticText(self.panel, label=_('Cell phone: '))
		self.textCell = TextCtrl(self.panel, value=cell, mask=self.formatCellPhone, style=wx.TE_PROCESS_ENTER)

		labelLandline = wx.StaticText(self.panel, label=_('Landline: '))
		self.textLandline = TextCtrl(
			self.panel, value=landline, mask=self.formatLandline, style=wx.TE_PROCESS_ENTER)

		labelEmail = wx.StaticText(self.panel, label=_('Email: '))
		self.textEmail = wx.TextCtrl(self.panel, value=email, size=(200, 25), style=wx.TE_PROCESS_ENTER)

		self.buttonOk = wx.Button(self.panel, wx.ID_OK, label=_('&Ok'))
		self.buttonOk.Bind(wx.EVT_BUTTON, self.onRecord)

		self.buttonCancel = wx.Button(self.panel, wx.ID_CANCEL, label=_('&Cancel'))
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

		email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}$'
		contactDict = {}

		Name = self.textName.GetValue().strip()
		Cell = self.textCell.GetValue().strip()
		Landline = self.textLandline.GetValue().strip()
		Email = self.textEmail.GetValue().strip()

		# Check the Name field
		if not Name:
			self.show_message(_('Name is required!'), _('Error'))
			self.textName.SetFocus()
			return None

		# Check the cell phone field
		if not Cell:
			self.show_message(_('Mobile number is required!'), _('Error'))
			self.textCell.SetFocus()
			return None

		# Check the Landline field
		if not Landline:
			self.show_message(_('Landline number is required!'), _('Error'))
			self.textLandline.SetFocus()
			return None

		# Check the Email field if it was provided
		if Email:
			if not re.match(email_regex, Email):
				self.show_message(_('Invalid email format!'), _('Error'))
				self.textEmail.SetFocus()
				return None
			Email = Email.replace("-", "")  # Remove hífen, se necessário

		# Fill the dictionary with the collected data
		contactDict['name'] = Name
		contactDict['cell'] = Cell
		contactDict['landline'] = Landline
		contactDict['email'] = Email

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

		# Check if contactDict is None
		if contactDict is None:
			return

		data = {'contacts': contactDict}
		try:
			core.add_record(data)

			# Translators:  Dialog displayed upon completion.
			message = _('Contact added, want to add a new contact?')
			caption = _('Success')

			user_response = gui.messageBox(message, caption, style=wx.ICON_QUESTION | wx.YES_NO)
			if user_response == wx.YES:
				# Clear all fields to add a new record.
				for child in self.panel.GetChildren():
					if isinstance(child, wx.TextCtrl):
						child.SetValue("")
			else:
				self.Destroy()
		except Exception as e:
			self.show_message(_('Error adding contact: {}').format(str(e)), _('Error'), wx.ICON_ERROR)

	# Cancels the dialog.
	def onClose(self, event):
		"""
		closes the window.

		Args:
			event (wx.Event): Event triggered by the cancel button.
		"""
		self.Destroy()

	def onEdit(self):
		"""
		Edits the selected contact in the database and displays a success message to the user.

		This method collects the form data,
		updates the contact in the database based on the selected contact, and then presents a dialog box to inform
		the user that the edit was successful.

		Returns:
			None
		"""

		contactDict = self.getData()
		core.edit_record(self.selectedRow.id, contactDict)

		# Translators:  Dialog displayed after editing is complete.
		self.show_message(_('Contact edited!'), _('Success'), wx.ICON_INFORMATION)
		self.Destroy()

	def onRecord(self, event):
		"""
Adds or edits a contact based on the form's current state.

		This method checks whether the form is in add or edit mode. Depending on the mode, it calls `onAdd()` to
		add a new contact or `onEdit()` to edit the existing contact.
		After the operation, the focus is set on the name field.

		Args:
			event (wx.Event): The event that triggered this method. This could be a click event or another type of
			user interaction.

		Returns:
			None
		"""

		if self.addRecord:
			self.onAdd()
		else:
			self.onEdit()
		self.textName.SetFocus()

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