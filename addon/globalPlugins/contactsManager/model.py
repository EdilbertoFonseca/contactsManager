# -*- coding: UTF-8 -*-

# Description: Database modeling for Contacts Manager for NVDA.

# Author: Edilberto Fonseca
# Email: <edilberto.fonseca@outlook.com>
# Copyright (C) 2022-2025 Edilberto Fonseca
# This file is covered by the GNU General Public License.
# See the file COPYING for more details or visit https://www.gnu.org/licenses/gpl-2.0.html.

# Date of creation: 30/11/2022.

# Imports necessary for the add-on to function.
import os
import sys

import versionInfo
from logHandler import log

from .configPanel import db_config  # Imports the instance of the DatabaseConfig class

# Get the path to the root of the current add-on
addonPath = os.path.dirname(__file__)

# Add the lib/ folder to sys.path (only once)
libPath = os.path.join(addonPath, "lib")
if libPath not in sys.path:
	sys.path.insert(0, libPath)

try:
	if versionInfo.version_year < 2024:
		import sqlite3 as sql
	else:
		import sqlite311 as sql
except ImportError as e:
	log.error(f"Error importing module: {str(e)}")


class ObjectContact(object):

	def __init__(self, id='', name='', cell='', landline='', email=''):
		"""
		Initializes a new contact with the provided details.

		Args:
			id (str): Unique contact identifier.
			name (str): Contact name.
			cell (str): Contact's cell phone number.
			landline (str): Contact's landline number.
			email (str): Contact email address.
		"""
		self.id = id
		self.name = name
		self.cell = cell
		self.landline = landline
		self.email = email

	def __repr__(self):
		"""
		Returns a formatted string representing the contact for Contact Manager for NVDA.

		Returns:
			str: A formatted string with the contact's name, cell phone, landline and email.
		"""
		return f'Name: {self.name}, Cell: {self.cell}, Landline: {self.landline}, Email: {self.email}'



class Section:
	connect = None
	cursor = None
	connected = False

	def __enter__(self):
		"""Método de entrada para o gerenciador de contexto."""
		self.connect = sql.connect(db_config.get_current_database_path())
		self.connect.row_factory = self.dict_factory # Adicionado aqui para consistência
		self.cursor = self.connect.cursor()
		self.connected = True
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Método de saída para o gerenciador de contexto."""
		if self.connect:
			self.connect.close()
		self.connected = False
		return False
	
	# Métodos connection e disconnect foram removidos.

	def execute(self, sql, parms=None):
		"""Executa uma consulta SQL no banco de dados."""
		if self.connected:
			if parms is None:
				self.cursor.execute(sql)
			else:
				self.cursor.execute(sql, parms)
			return True
		return False

	def executemany(self, sql, parms=None):
		"""Executa várias consultas SQL no banco de dados."""
		if self.connected:
			if parms is None:
				self.cursor.executemany(sql)
			else:
				self.cursor.executemany(sql, parms)
			return True
		return False

	def dict_factory(self, cursor, row):
		"""Converte o resultado de uma consulta em um dicionário."""
		return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

	def fetchall(self):
		"""Recupera todas as linhas do resultado de uma consulta."""
		# A linha self.connect.row_factory = self.dict_factory foi movida para o __enter__
		return self.cursor.fetchall()

	def persist(self):
		"""Confirma as alterações feitas em uma transação de banco de dados."""
		if self.connected:
			self.connect.commit()
			return True
		return False

	@classmethod
	def initDB(cls):
		"""Verifica a existência do banco de dados e cria a tabela de contatos, se não existir."""
		with cls() as trans:
			sqlCommand = """CREATE TABLE IF NOT EXISTS contacts(
				id INTEGER PRIMARY KEY, name TEXT, cell TEXT, landline TEXT, email TEXT)"""
			trans.execute(sqlCommand)
			trans.persist()
