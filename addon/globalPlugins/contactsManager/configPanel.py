# -*- coding: UTF-8 -*-

# Description: Contacts manager configuration panel.
# Author: Edilberto Fonseca.
# Email: edilberto.fonseca@outlook.com.
# Date of creation: 24/01/2023.

# Imports necessary for the add-on to function.
import logging
import os

import addonHandler
import addonHandler.addonVersionCheck
import config
import gui
import wx
from gui import guiHelper
from gui.settingsDialogs import SettingsPanel

from .varsConfig import initConfiguration, ourAddon

# For the translation process
addonHandler.initTranslation()

# Get a logger with the name of the current module
logger = logging.getLogger(__name__)

# Get the summary of the manifest
addonSummary = addonHandler.getCodeAddon().manifest["summary"]

# Initialize settings
initConfiguration()


class DatabaseConfig:

	def __init__(self, default_path):
		self.default_path = default_path
		self.first_database = default_path
		self.alt_database = ""
		self.index_db = 0
		self.load_config()

	def load_config(self):
		try:
			self.index_db = int(config.conf[ourAddon.name].get("xx", 0))
			if self.index_db == 0:
				self.first_database = config.conf[ourAddon.name].get("path", self.default_path)
			else:
				self.alt_database = config.conf[ourAddon.name].get("altPath", self.default_path)
		except ValueError:
			logger.error("Invalid value for database index in configuration, using default.")
		except KeyError:
			logger.warning("Database configuration not found, using default paths.")

	def save_config(self):
		config.conf[ourAddon.name]["path"] = self.first_database
		config.conf[ourAddon.name]["altPath"] = self.alt_database
		config.conf[ourAddon.name]["xx"] = str(self.index_db)

	def set_database_path(self, new_path, is_first=True):
		if is_first:
			self.first_database = new_path
		else:
			self.alt_database = new_path

	def get_current_database_path(self):
		return self.first_database if self.index_db == 0 else self.alt_database

	def update_database_path(self, new_path):
		"""
		Updates the database path and renames the old file if necessary.
		"""
		if self.index_db == 0:
			if os.path.exists(new_path):
				self.set_database_path(new_path, is_first=True)
			else:
				os.rename(self.first_database, new_path)
				self.set_database_path(new_path, is_first=True)
		else:
			if os.path.exists(new_path):
				self.set_database_path(new_path, is_first=False)
			else:
				if not self.alt_database:
					self.set_database_path(new_path, is_first=False)
				else:
					os.rename(self.alt_database, new_path)
					self.set_database_path(new_path, is_first=False)


# DatabaseConfig class instance
db_config = DatabaseConfig(default_path=os.path.join(os.path.dirname(__file__), "database.db"))


class ContactsManagerSettingsPanel(SettingsPanel):
	# Translators: Title of the Contacts Manager settings dialog in the NVDA settings.
	title = addonSummary

	def makeSettings(self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: Formatting text for phone fields.
		phoneFormattingBoxSizer = wx.StaticBoxSizer(wx.HORIZONTAL, self, label=_("Add mask for phone fields:"))
		phoneFormattingBox = phoneFormattingBoxSizer.GetStaticBox()
		phoneFormattingGroup = guiHelper.BoxSizerHelper(self, sizer=phoneFormattingBoxSizer)
		settingsSizerHelper.addItem(phoneFormattingGroup)

		# Cell field formatting.
		wx.StaticText(phoneFormattingBox, label=_("Cell phone"))
		self.textCellPhone = wx.TextCtrl(phoneFormattingBox, value="")
		self.textCellPhone.SetValue(config.conf[ourAddon.name].get("formatCellPhone", ""))

		# Formatting the landline phone field.
		wx.StaticText(phoneFormattingBox, label=_("Landline"))
		self.textLandline = wx.TextCtrl(phoneFormattingBox, value="")
		self.textLandline.SetValue(config.conf[ourAddon.name].get("formatLandline", ""))

		self.resetRecords = wx.CheckBox(
			# Translators: Checkbox text to display scheduler reset button.
			self, label=_('&Show option to delete entire calendar')
		)
		self.resetRecords.SetValue(config.conf[ourAddon.name].get("resetRecords", False))
		settingsSizerHelper.addItem(self.resetRecords)

		# Button to import CSV files.
		self.importCSV = wx.CheckBox(
			# Translators: Checkbox text to display import csv files to database.
			self, label=_('&Show import CSV file button')
		)
		self.importCSV.SetValue(config.conf[ourAddon.name].get("importCSV", False))
		settingsSizerHelper.addItem(self.importCSV)

		# Button to export CSV files.
		self.exportCSV = wx.CheckBox(
			# Translators: Checkbox text to display export csv files to database.
			self, label=_('&Show export CSV file button')
		)
		self.exportCSV.SetValue(config.conf[ourAddon.name].get("exportCSV", False))
		settingsSizerHelper.addItem(self.exportCSV)

		pathBoxSizer = wx.StaticBoxSizer(
			# Translators: Name of combobox with the agenda files path.
			wx.HORIZONTAL, self, label=_("Path of agenda files:")
		)
		pathBox = pathBoxSizer.GetStaticBox()
		pathGroup = guiHelper.BoxSizerHelper(self, sizer=pathBoxSizer)
		settingsSizerHelper.addItem(pathGroup)

		self.pathList = [db_config.first_database, db_config.alt_database]
		self.pathNameCB = pathGroup.addLabeledControl("", wx.Choice, choices=self.pathList)
		self.pathNameCB.SetSelection(db_config.index_db)

		# Translators: This is the label for the button used to add or change a contactsManager.db location.
		changePathBtn = wx.Button(pathBox, label=_("&Select or add a directory"))
		changePathBtn.Bind(wx.EVT_BUTTON, self.OnDirectory)

	def OnDirectory(self, event):
		"""
		Selects a directory to save the database file.
		"""

		self.Freeze()
		lastDir = os.path.dirname(__file__)
		dDir = lastDir
		dFile = "database.db"
		frame = wx.Frame(None, -1, 'teste')
		frame.SetSize(0, 0, 200, 50)
		dlg = wx.FileDialog(
			frame,
			_("Choose where to save the Data Base file"),
			dDir,
			dFile,
			wildcard=_("Database files (*.db)"),
			style=wx.FD_SAVE
		)
		if dlg.ShowModal() == wx.ID_OK:
			fname = dlg.GetPath()
			index = self.pathNameCB.GetSelection()
			db_config.index_db = index
			db_config.update_database_path(fname)

			# Update the combobox choices and selection
			self.pathList = [db_config.first_database, db_config.alt_database]
			self.pathNameCB.Set(self.pathList)
			self.pathNameCB.SetSelection(index)

		dlg.Close()
		frame.Destroy()
		self.onPanelActivated()
		self._sendLayoutUpdatedEvent()
		self.Thaw()
		event.Skip()

	def onSave(self):
		"""
		Saves the options to the NVDA configuration file.
		"""

		config.conf[ourAddon.name]["formatCellPhone"] = self.textCellPhone.GetValue()
		config.conf[ourAddon.name]["formatLandline"] = self.textLandline.GetValue()
		config.conf[ourAddon.name]["resetRecords"] = self.resetRecords.GetValue()
		config.conf[ourAddon.name]["importCSV"] = self.importCSV.GetValue()
		config.conf[ourAddon.name]["exportCSV"] = self.exportCSV.GetValue()

		# Update selection index and save settings
		db_config.index_db = self.pathNameCB.GetSelection()
		db_config.save_config()

		# Reactivate profiles triggers
		config.conf.enableProfileTriggers()

	def onPanelActivated(self):
		"""
		Disables all profile triggers and active profiles, and displays the settings panel.

This method is called when the settings panel is activated. First, it disables all profile triggers, which
are used to trigger specific events or behaviors based on profile settings. Then the method displays
the settings panel in the user interface.

		Returns:
			None
		"""
		config.conf.disableProfileTriggers()
		self.Show()

	def onPanelDeactivated(self):
		"""
		Re-enables profile triggers and hides the settings panel.

		This method is called when the settings panel is disabled. First, it reactivates profile triggers,
		which are used to trigger specific events or behaviors based on profile settings. Then the method hides
		the UI settings panel.

		Returns:
			None
		"""
		config.conf.enableProfileTriggers()
		self.Hide()

	def terminate(self):
		"""
Ends the Contact Manager settings panel.

		This method is called when the Contact Manager settings panel is being closed or disabled. First, it calls
		the superclass's `terminate()` method to ensure that any cleanup or termination performed by the
		superclass is also performed. It then calls the `onPanelDeactivated()` method to perform any additional
		actions required when the panel is deactivated.

		Returns:
			None
		"""
		super(ContactsManagerSettingsPanel, self).terminate()
		self.onPanelDeactivated()
