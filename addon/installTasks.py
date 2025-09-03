# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 03/03/2023.
"""

import os

import addonHandler
import config
import globalVars
from gui import messageBox

# For translation process
addonHandler.initTranslation()

# Get the name of the addon defined in the manifest.
ADDON_name = addonHandler.getCodeAddon().manifest["name"]

def onInstall():
	"""
	Moves the add-on database file to a new location during installation.
	"""
	relativeDbPath = os.path.join("addons", "contactsManager", "globalPlugins", "contactsManager", "database.db")
	absoluteDbPath = os.path.abspath(os.path.join(globalVars.appArgs.configPath, relativeDbPath))

	if os.path.isfile(absoluteDbPath):
		configPath = globalVars.appArgs.configPath
		addonRelativePath = os.path.join("addons", "contactsManager")
		dbRelativeSuffix = os.path.join("globalPlugins", "contactsManager", "database.db")
		newDbPath = os.path.join(configPath, addonRelativePath + addonHandler.ADDON_PENDINGINSTALL_SUFFIX, dbRelativeSuffix)

		try:
			os.rename(absoluteDbPath, os.path.abspath(newDbPath))
		except OSError as e:
			messageBox(_(f"Error when renaming file: {e}"), _("Attention"))


def onUninstall():
	# Go through the configuration profiles and try to remove the 'Contacts Manager for NVDA' key
	for key, value in list(config.conf._profileCache.items()):
		try:
			del config.conf._profileCache[key][ADDON_name]
		except KeyError:
			pass  # Ignore if key does not exist

	# Save configuration changes
	config.conf.save()
