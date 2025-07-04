# -*- coding: UTF-8 -*-

# Description: Variables for the Contacts Manager for NVDA add-on

# Author: Edilberto Fonseca
# Email: <edilberto.fonseca@outlook.com>
# Copyright (C) 2022-2025 Edilberto Fonseca
# This file is covered by the GNU General Public License.
# See the file COPYING for more details or visit https://www.gnu.org/licenses/gpl-2.0.html.

# Date of creation: 24/05/2024

# Import the necessary modules

import addonHandler
import config
from logHandler import log

# Get the title of the add-on defined in the summary.
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

def getOurAddon():
	"""
	Retrieves the current add-on.
	Returns:
		addonHandler.Addon: The current add-on instance.
	"""
	try:
		return addonHandler.getCodeAddon()
	except Exception as e:
		log.error(f"Error getting the add-on: {e}")


# Retrieve the current add-on instance
ourAddon = getOurAddon()


def initConfiguration():
	"""
	Initializes the configuration specification for the Contacts Manager for NVDA add-on.
	"""
	try:
		confspec = {
			"formatCellPhone": """string(default="(##) #####-####")""",
			"formatLandline": """string(default="(##) ####-####")""",
			"resetRecords": "boolean(default=True)",
			"importCSV": "boolean(default=True)",
			"exportCSV": "boolean(default=True)",
			"path": "string(default="")",
			"altPath": "string(default="")",
			"xx": "string(default="")",
		}
		config.conf.spec[ourAddon.name] = confspec
	except Exception as e:
		log.error(f"Error initializing configuration: {e}")


# Initialize the configuration
initConfiguration()
