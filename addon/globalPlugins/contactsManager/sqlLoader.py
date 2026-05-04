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

Created on: 19/02/2026
"""

import os
import sys
from typing import Any

from logHandler import log

from .varsConfig import ADDON_PATH, IS64

libFolder = "lib64" if IS64 else "lib"
libPath = os.path.join(ADDON_PATH, libFolder)

# Adding library path to sys.path
if os.path.isdir(libPath) and libPath not in sys.path:
	sys.path.insert(0, libPath)

# We initialize the sql variable to None to help the linter
sql: Any = None

try:
	if sys.version_info >= (3, 11):
		try:
			import sqlite311 as sql

			log.info("Loaded sqlite311 custom module.")
		except ImportError:
			import sqlite3 as sql

			log.warning("Fallback to builtin sqlite3 (3.11+).")
	else:
		# Python 3.7
		import sqlite3 as sql

		log.info("Loaded builtin sqlite3 (3.7).")

except ImportError as e:
	log.error(f"Failed to load any sqlite module: {e}", exc_info=True)
	raise

# Security check (optional)
if sql is None:
	raise ImportError("Sqlite module could not be initialized.")
