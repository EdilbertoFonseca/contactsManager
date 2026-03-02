# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 19/02/2026
"""

import os
import sys
from logHandler import log
from .varsConfig import ADDON_PATH, is64

libFolder = "lib64" if is64 else "lib"
libPath = os.path.join(ADDON_PATH, libFolder)

if os.path.isdir(libPath) and libPath not in sys.path:
	sys.path.insert(0, libPath)

try:
	# Python 3.11+
	if sys.version_info >= (3, 11):
		try:
			import sqlite311 as sql
			log.info("Loaded sqlite311 custom module.")
		except ImportError:
			import sqlite3 as sql
			log.warning("Fallback to builtin sqlite3 (3.11+).")
	else:
		# Python 3.7
		try:
			import sqlite3 as sql
			log.info("Loaded builtin sqlite3 (3.7).")
		except ImportError:
			raise

except ImportError as e:
	log.error(f"Failed to load any sqlite module: {e}")
	raise
