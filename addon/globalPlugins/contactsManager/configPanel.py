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

Created on: 24/01/2023.
"""

import os

import addonHandler
import addonHandler.addonVersionCheck
import config
import gui
import wx
from gui import guiHelper
from gui.settingsDialogs import SettingsPanel
from logHandler import log

from .varsConfig import ADDON_SUMMARY, initConfiguration, ourAddon, countryCode

# Initialize translation support
addonHandler.initTranslation()

# Initialize settings
initConfiguration()


class DatabaseConfig:

	def __init__(self, defaultPath):
		self.defaultPath = defaultPath
		self.firstDatabase = defaultPath
		self.altDatabase = ""
		self.indexDb = 0
		self.loadConfig()

	def loadConfig(self):
		try:
			self.indexDb = int(config.conf[ourAddon.name].get("selectedDBIndex", 0))
			if self.indexDb == 0:
				self.firstDatabase = config.conf[ourAddon.name].get("currentDBPath", self.defaultPath)
			else:
				self.altDatabase = config.conf[ourAddon.name].get("alternateDBPath", self.defaultPath)
		except ValueError:
			log.error("Invalid value for database index in configuration, using default.")
		except KeyError:
			log.warning("Database configuration not found, using default paths.")

	def saveConfig(self):
		config.conf[ourAddon.name]["currentDBPath"] = self.firstDatabase
		config.conf[ourAddon.name]["alternateDBPath"] = self.altDatabase
		config.conf[ourAddon.name]["selectedDBIndex"] = str(self.indexDb)

	def setDatabasePath(self, newPath, isFirst=True):
		if isFirst:
			self.firstDatabase = newPath
		else:
			self.altDatabase = newPath

	def getCurrentDatabasePath(self):
		return self.firstDatabase if self.indexDb == 0 else self.altDatabase

	def updateDatabasePath(self, newPath):
		"""
		Updates the database currentDBPath and renames the old file if necessary.
		"""
		if self.indexDb == 0:
			if os.path.exists(newPath):
				self.setDatabasePath(newPath, isFirst=True)
			else:
				os.rename(self.firstDatabase, newPath)
				self.setDatabasePath(newPath, isFirst=True)
		else:
			if os.path.exists(newPath):
				self.setDatabasePath(newPath, isFirst=False)
			else:
				if not self.altDatabase:
					self.setDatabasePath(newPath, isFirst=False)
				else:
					os.rename(self.altDatabase, newPath)
					self.setDatabasePath(newPath, isFirst=False)


# DatabaseConfig class instance
dbConfig = DatabaseConfig(defaultPath=os.path.join(os.path.dirname(__file__), "database.db"))


class ContactsManagerSettingsPanel(SettingsPanel):
	# Translators: Title of the Contacts Manager settings dialog in the NVDA settings.
	title = ADDON_SUMMARY

	def makeSettings(self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: Formatting text for phone fields.
		phoneFormattingBoxSizer = wx.StaticBoxSizer(
			wx.HORIZONTAL,
			self,
			label=_("Add mask for phone fields:")
		)

		phoneFormattingBox = phoneFormattingBoxSizer.GetStaticBox()
		phoneFormattingGroup = guiHelper.BoxSizerHelper(self, sizer=phoneFormattingBoxSizer)
		settingsSizerHelper.addItem(phoneFormattingGroup)

		# Country code
		choices = [f"{code} - {name}" for code, name in countryCode]
		self.countryCode = phoneFormattingGroup.addLabeledControl(
			_("Country code"),
	wx.ComboBox,
	choices=choices,
			style=wx.CB_READONLY
		)
		savedCode = config.conf[ourAddon.name].get("countryCode", "55")

		for i, (code, name) in enumerate(countryCode):
			if code == savedCode:
				self.countryCode.SetSelection(i)
				break

		# Cell phone
		self.textCellPhone = phoneFormattingGroup.addLabeledControl(
			_("Cell phone"),
			wx.TextCtrl
		)
		self.textCellPhone.SetValue(
			config.conf[ourAddon.name].get("formatCellPhone", "")
		)

		# Landline
		self.textLandline = phoneFormattingGroup.addLabeledControl(
			_("Landline"),
			wx.TextCtrl
		)
		self.textLandline.SetValue(
			config.conf[ourAddon.name].get("formatLandline", "")
		)

		# Group for buttons
		buttonsBoxSizer = wx.StaticBoxSizer(
			wx.VERTICAL,
			self,
			# Translators: Group for buttons
			label=_("Options")
		)

		buttonsBox = buttonsBoxSizer.GetStaticBox()
		buttonsGroup = guiHelper.BoxSizerHelper(self, sizer=buttonsBoxSizer)

		settingsSizerHelper.addItem(buttonsGroup)

		# Buttons within the group
		self.resetRecords = buttonsGroup.addItem(
			# Translators: Label for the checkbox to show the option to delete the entire calendar.
			wx.CheckBox(buttonsBox, label=_("Show option &to delete entire calendar"))
		)
		self.resetRecords.SetValue(
			config.conf[ourAddon.name].get("resetRecords", False)
		)

		self.importCSV = buttonsGroup.addItem(
			# Translators: Label for the checkbox to show the import CSV file button.
			wx.CheckBox(buttonsBox, label=_("Show &import CSV file button"))
		)
		self.importCSV.SetValue(
			config.conf[ourAddon.name].get("importCSV", False)
		)

		self.exportCSV = buttonsGroup.addItem(
			# Translators: Label for the checkbox to show the export CSV file button.
			wx.CheckBox(buttonsBox, label=_("Show e&xport CSV file button"))
		)
		self.exportCSV.SetValue(
			config.conf[ourAddon.name].get("exportCSV", False)
		)

		pathBoxSizer = wx.StaticBoxSizer(
			# Translators: Name of combobox with the agenda files currentDBPath.
			wx.HORIZONTAL, self, label=_("Path of agenda files:")
		)
		pathBox = pathBoxSizer.GetStaticBox()
		pathGroup = guiHelper.BoxSizerHelper(self, sizer=pathBoxSizer)
		settingsSizerHelper.addItem(pathGroup)

		self.pathList = [dbConfig.firstDatabase, dbConfig.altDatabase]
		self.pathNameCB = pathGroup.addLabeledControl("", wx.Choice, choices=self.pathList)
		self.pathNameCB.SetSelection(dbConfig.indexDb)

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
		frame = wx.Frame(None, -1, "teste")
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
			dbConfig.indexDb = index
			dbConfig.updateDatabasePath(fname)

			# Update the combobox choices and selection
			self.pathList = [dbConfig.firstDatabase, dbConfig.altDatabase]
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

		selection = self.countryCode.GetSelection()

		if selection != wx.NOT_FOUND:
			code = countryCode[selection][0]

		config.conf[ourAddon.name]["countryCode"] = code
		config.conf[ourAddon.name]["formatCellPhone"] = self.textCellPhone.GetValue()
		config.conf[ourAddon.name]["formatLandline"] = self.textLandline.GetValue()
		config.conf[ourAddon.name]["resetRecords"] = self.resetRecords.GetValue()
		config.conf[ourAddon.name]["importCSV"] = self.importCSV.GetValue()
		config.conf[ourAddon.name]["exportCSV"] = self.exportCSV.GetValue()

		# Update selection index and save settings
		dbConfig.indexDb = self.pathNameCB.GetSelection()
		dbConfig.saveConfig()

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
