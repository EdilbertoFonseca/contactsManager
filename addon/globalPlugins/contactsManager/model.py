# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 30/11/2022.
"""

from .configPanel import db_config  # Imports the instance of the DatabaseConfig class
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
		"""Input method for the context manager."""
		self.connect = sql.connect(db_config.get_current_database_path())
		self.connect.row_factory = self.dict_factory # Adicionado aqui para consistência
		self.cursor = self.connect.cursor()
		self.connected = True
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""Output method for the context manager."""
		if self.connect:
			self.connect.close()
		self.connected = False
		return False
	
	# Connection and disconnect methods have been removed.

	def execute(self, sql, parms=None):
		"""Executes an SQL query on the database."""
		if self.connected:
			if parms is None:
				self.cursor.execute(sql)
			else:
				self.cursor.execute(sql, parms)
			return True
		return False

	def executemany(self, sql, parms=None):
		"""Executes multiple SQL queries against the database."""
		if self.connected:
			if parms is None:
				self.cursor.executemany(sql)
			else:
				self.cursor.executemany(sql, parms)
			return True
		return False

	def dict_factory(self, cursor, row):
		"""Converts the result of a query to a dictionary."""
		return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

	def fetchall(self):
		"""Recupera todas as linhas do resultado de uma consulta."""
		# A linha self.connect.row_factory = self.dict_factory foi movida para o __enter__
		return self.cursor.fetchall()

	def persist(self):
		"""Commits changes made to a database transaction."""
		if self.connected:
			self.connect.commit()
			return True
		return False

	@classmethod
	def initDB(cls):
		"""Checks the existence of the database and creates the contact table if it does not exist."""
		with cls() as trans:
			sqlCommand = """CREATE TABLE IF NOT EXISTS contacts(
				id INTEGER PRIMARY KEY, name TEXT, cell TEXT, landline TEXT, email TEXT)"""
			trans.execute(sqlCommand)
			trans.persist()
