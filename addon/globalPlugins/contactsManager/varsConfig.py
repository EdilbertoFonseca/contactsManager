# -*- coding: UTF-8 -*-

# Description: Variables for the Contacts Manager for NVDA add-on
# Author: Edilberto Fonseca
# Email: edilberto.fonseca@outlook.com
# Date of creation: 24/05/2024
# Copyright (C) 2022-2023 Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Import the necessary modules
import logging

import addonHandler
import config

# Configure the logger instance for the current module, allowing logging of log messages.
logger = logging.getLogger(__name__)


def getOurAddon():
	"""
	Retrieves the current add-on.
	Returns:
		addonHandler.Addon: The current add-on instance.
	"""
	try:
		return addonHandler.getCodeAddon()
	except Exception as e:
		logger.error(f"Error getting the add-on: {e}")


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
		logger.error(f"Error initializing configuration: {e}")


# Initialize the configuration
initConfiguration()