# -*- coding: UTF-8 -*-

# Description:
# Database modeling for Contacts Manager for NVDA.

# Author: Edilberto Fonseca
# Email: <edilberto.fonseca@outlook.com>
# Copyright (C) 2022-2025 Edilberto Fonseca
# This file is covered by the GNU General Public License.
# See the file COPYING for more details or visit https://www.gnu.org/licenses/gpl-2.0.html.

# Date of creation: 30/11/2022.

# Imports necessary for the add-on to function.
import logging
import os
import sys

import versionInfo

from .configPanel import db_config  # Imports the instance of the DatabaseConfig class

# Get a logger with the name of the current module
logger = logging.getLogger(__name__)

# Add directories to sys.path before importing libraries
baseDir = os.path.dirname(__file__)
libs = os.path.join(baseDir, "lib")
sys.path.append(libs)
try:
	if versionInfo.version_year < 2024:
		import sqlite3 as sql
	else:
		import sqlite311 as sql
except ImportError as e:
	logger.error(f"Error importing module: {str(e)}")


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

	@classmethod
	def connection(cls):
		"""Conecta ao banco de dados usando o caminho atual."""
		cls.connect = sql.connect(db_config.get_current_database_path())  # Usa o caminho atual do banco de dados
		cls.cursor = cls.connect.cursor()
		cls.connected = True

	def disconnect(self):
		"""Desconecta do banco de dados."""
		if Section.connect:
			Section.connect.close()
			Section.connected = False

	def execute(self, sql, parms=None):
		"""Executa uma consulta SQL no banco de dados."""
		if Section.connected:
			if parms is None:
				Section.cursor.execute(sql)
			else:
				Section.cursor.execute(sql, parms)
			return True
		return False

	def executemany(self, sql, parms=None):
		"""Executa várias consultas SQL no banco de dados."""
		if Section.connected:
			if parms is None:
				Section.cursor.executemany(sql)
			else:
				Section.cursor.executemany(sql, parms)
			return True
		return False

	def dict_factory(self, cursor, row):
		"""Converte o resultado de uma consulta em um dicionário."""
		return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

	def fetchall(self):
		"""Recupera todas as linhas do resultado de uma consulta."""
		Section.cursor.row_factory = self.dict_factory
		return Section.cursor.fetchall()

	def persist(self):
		"""Confirma as alterações feitas em uma transação de banco de dados."""
		if Section.connected:
			Section.connect.commit()
			return True
		return False

	def __enter__(self):
		"""Método de entrada para o gerenciador de contexto."""
		self.connection()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Método de saída para o gerenciador de contexto."""
		self.disconnect()
		# Se não quiser suprimir exceções, retorne False.
		return False

	@classmethod
	def initDB(cls):
		"""Verifica a existência do banco de dados e cria a tabela de contatos, se não existir."""
		with cls() as trans:
			sqlCommand = """CREATE TABLE IF NOT EXISTS contacts(
				id INTEGER PRIMARY KEY, name TEXT, cell TEXT, landline TEXT, email TEXT)"""
			trans.execute(sqlCommand)
			trans.persist()
