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

Created on: 30/11/2022
"""

import os
from functools import partial
import addonHandler
import globalPluginHandler
import globalVars
import gui
import wx
from logHandler import log
from scriptHandler import script

from .configPanel import ContactsManagerSettingsPanel
from .main import ContactList
from .model import Section
from .varsConfig import ADDON_SUMMARY, initConfiguration

# Initialize configuration settings
initConfiguration()

# Start the initDB function.
Section.initDB()

# Initialize translation support
addonHandler.initTranslation()

def disableInSecureMode(decoratedCls):
	"""
	Decorates a class to disable the plugin if safe mode is enabled.

	Args:
		decoratedCls (type): The class to be decorated.

	Returns:
		type: Retorna `globalPluginHandler.GlobalPlugin` if safe mode is enabled; otherwise, returns the decorated
		class.
	"""

	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Creating the constructor of the newly created GlobalPlugin class.
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.createMenu()

	def createMenu(self):
		"""
		Creates and adds the contact management menu to the main menu.

		Adds the contact manager settings panel to the list of settings categories.
		Creates the main menu and submenus for contact manager, settings, and help.
		Adds the main menu to the system tray icon tools menu.
		"""
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(ContactsManagerSettingsPanel)
		self.mainMenu = wx.Menu()
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu

		self.contactsManager = self.mainMenu.Append(-1, _('&Contact List'))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_activateContactsManager, self.contactsManager)

		self.settingsPanel = self.mainMenu.Append(-1, _('&Settings'))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_openAddonSettingsDialog, self.settingsPanel)

		self.help = self.mainMenu.Append(-1, _('&Help'))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_onHelp, self.help)

		# Save submenu item
		self.contactsManagerMenuItem = self.toolsMenu.AppendSubMenu(self.mainMenu, "&{}...".format(ADDON_SUMMARY))

	def onContactsManager(self, event):
		"""
		Opens the contact list window.

		Args:
			event (wx.Event): The event triggered by the contactsManager button.
		"""
		# Translators: Title of contact list dialog box.
		wx.CallAfter(self.displayDialog, ContactList, "dlgContact", _('Contact list.'))

	# defining a script with decorator:
	@script(
		gesture='kb:Windows+alt+L',
		# Translators: Text displayed in NVDA help.
		description=_('Displays a window with all contacts registered in the Contacts Manager.'),
		category=ADDON_SUMMARY
	)
	def script_activateContactsManager(self, gesture):
		wx.CallAfter(self.onContactsManager, None)

	# defining a script with decorator:
	@script(
		gesture='kb:Windows+alt+O',
		# Translators: Opens the Contacts Manager configuration menu
		description=_("Opens Contacts Manager add-on settings"),
		category=ADDON_SUMMARY
	)
	@gui.blockAction.when(gui.blockAction.Context.MODAL_DIALOG_OPEN)
	def script_openAddonSettingsDialog(self, gesture):
		wx.CallAfter(
			getattr(gui.mainFrame, "popupSettingsDialog", gui.mainFrame._popupSettingsDialog),
			gui.settingsDialogs.NVDASettingsDialog,
			ContactsManagerSettingsPanel
		)

	# defining a script with decorator:
	@script(
		gesture='kb:Windows+alt+J',
		# Translators: Text displayed in NVDA help.
		description=_('Opens the Contacts Manager add-on help page.'),
		category=ADDON_SUMMARY
	)
	def script_onHelp(self, gesture):
		"""Open the addon's help page"""
		wx.LaunchDefaultBrowser(addonHandler.Addon(os.path.join(
			os.path.dirname(__file__), "..", "..")).getDocFilePath())

	def _onDestroy(self, e: wx.Event, attrName: str) -> None:
		self.onGenericClosed(e, attrName)

	def displayDialog(self, dialogClass, attrName, *args, **kwargs):
		# 1. Retrieves what is stored in the attribute
		dlg = getattr(self, attrName, None)

		# 2. "Life" check:
		# If None OR if the wx object is no longer valid (window closed)
		if dlg is None or not dlg:
			# We create a new instance
			dlg = dialogClass(gui.mainFrame, *args, **kwargs)
			setattr(self, attrName, dlg)

			# We bind the attribute cleanup when the window is destroyed
			dlg.Bind(wx.EVT_WINDOW_DESTROY, partial(self._onDestroy, attrName=attrName))

		# 3. Display and Focus
		try:
			gui.mainFrame.prePopup()

			# We check once again if the object is active before calling methods
			if dlg:
				if dlg.IsIconized():
					dlg.Restore()
				dlg.Show()
				dlg.Raise()
				dlg.SetFocus()

			gui.mainFrame.postPopup()
		except Exception as e:
			log.error(f"Error when manipulating window {attrName}: {e}")
			setattr(self, attrName, None)

	def onGenericClosed(self, evt: wx.Event, attrName: str) -> None:
		"""Handles the closure of generic dialogs."""
		setattr(self, attrName, None)
		evt.Skip()

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(
			ContactsManagerSettingsPanel)
		try:
			self.toolsMenu.Remove(self.contactsManagerMenuItem)
		except Exception as e:
			log.warning(f"Error removing Scraps and agenda organizer menu item: {e}")
