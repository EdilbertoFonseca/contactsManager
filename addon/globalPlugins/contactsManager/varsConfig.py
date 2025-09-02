# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 24/05/2024
"""

import os

import addonHandler
import config
from logHandler import log

# Get the path to the root of the current add-on
ADDON_PATH = os.path.dirname(__file__)

# Get the title of the add-on defined in the summary.
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

# Retrieve the current add-on instance
try:
	ourAddon = addonHandler.getCodeAddon()
except Exception as e:
	log.error(f"Error getting the add-on: {e}")

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
			"currentDBPath": "string(default="")",
			"alternateDBPath": "string(default="")",
			"selectedDBIndex": "string(default="")",
		}
		config.conf.spec[ourAddon.name] = confspec
	except Exception as e:
		log.error(f"Error initializing configuration: {e}")


# Initialize the configuration
initConfiguration()
