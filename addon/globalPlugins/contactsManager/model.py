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

Created on: 30/11/2022.
"""

import os
import sys

import versionInfo
from logHandler import log

from .configPanel import dbConfig  # Imports the instance of the DatabaseConfig class
from .sqlLoader import sql


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
		self.connect = sql.connect(dbConfig.getCurrentDatabasePath())
		self.connect.row_factory = self.dictFactory # Adicionado aqui para consistência
		self.cursor = self.connect.cursor()
		self.connected = True
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Método de saída para o gerenciador de contexto."""
		if self.connect:
			self.connect.close()
		self.connected = False
		return False

	# Connection and disconnect methods have been removed.

	def execute(self, sql, parms=None):
		"""Executa uma consulta SQL no banco de dados."""
		if self.connected:
			if parms is None:
				self.cursor.execute(sql)
			else:
				self.cursor.execute(sql, parms)
			return True
		return False

	def executeMany(self, sql, parms=None):
		"""Executa várias consultas SQL no banco de dados."""
		if self.connected:
			if parms is None:
				self.cursor.executemany(sql)
			else:
				self.cursor.executemany(sql, parms)
			return True
		return False

	def dictFactory(self, cursor, row):
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
		try:
			with cls() as trans:
				# Garante que a tabela existe com a estrutura completa
				sqlCommand = """CREATE TABLE IF NOT EXISTS contacts(
					id INTEGER PRIMARY KEY AUTOINCREMENT, 
					name TEXT NOT NULL, 
					cell TEXT, 
					landline TEXT, 
					email TEXT)"""
				trans.execute(sqlCommand)
				trans.persist()
				log.info("ContactsManager: Base de dados inicializada com sucesso.")
		except Exception as e:
			log.error(f"ContactsManager: Erro ao inicializar base de dados: {e}")
			

# Start the initDB function.
Section.initDB()
