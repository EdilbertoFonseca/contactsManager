# -*- coding: UTF-8 -*-

"""
Author: Edilberto Fonseca <edilberto.fonseca@outlook.com>
Copyright: (C) 2025 Edilberto Fonseca

This file is covered by the GNU General Public License.
See the file COPYING for more details or visit:
https://www.gnu.org/licenses/gpl-2.0.html

Created on: 30/11/2022.
"""

import os
import sys

import addonHandler
from logHandler import log

from .model import ObjectContact, Section
from .varsConfig import ADDON_PATH

# Get the path to the root of the current add-on
# Add the lib/ folder to sys.path (only once)
libPath = os.path.join(ADDON_PATH, "lib")
if libPath not in sys.path:
	sys.path.insert(0, libPath)

try:
	import csv
except ImportError as e:
	log.error(f"Error importing module: {str(e)}")

# Initialize translation support
addonHandler.initTranslation()
def get_all_records():
	"""
	Function that retrieves all data from the database.

	This function queries the database to obtain all stored records
	in the contact table, sorted alphabetically by name. The results are converted
	into `ObjectContact` objects and returned as a list.

	Returns:
		list: A list of `ObjectContact` objects representing all records in the database.
	"""
	with Section() as trans:
		trans.execute("SELECT * FROM contacts ORDER BY name ASC")
		results = trans.fetchall()
	return convert_results(results)


def convert_results(results):
	"""
	Converts the results to `ObjectContact` objects.

	Esta função recebe uma lista de resultados de codatabase query, where each result is a dictionary,
	and converts these results into `ObjectContact` objects.

	Args:
		results (list): A list of dictionaries, where each dictionary represents a contact record.

	Returns:
		list: A list of `ObjectContact` objects, where each object represents a contact in the database.
	"""

	rows = [ObjectContact(
		record['id'], record['name'], record['cell'], record['landline'], record['email']) for record in results]
	return rows


def add_record(data):
	"""
	Inserts new records into the database.

	This function receives a dictionary containing information about a new contact and inserts it into the
	database.

	Args:
		data (dict): A dictionary containing the contact information to be inserted.
			The expected keys in the dictionary are:
				- 'name' (str): Contact name.
				- 'cell' (str): Contact's cell phone number.
				- 'landline' (str): Contact's landline number.
				- 'email' (str): Contact email address.
	"""

	with Section() as trans:
		trans.execute(
			"INSERT INTO contacts VALUES(NULL, ?,?,?,?)", (data["contacts"]["name"], data['contacts']['cell'], data['contacts']['landline'], data['contacts']['email']))
		trans.persist()


def search_records(filterChoice, keyword):
	"""
	Searches for records in the database based on the chosen filter and the keyword provided by the user.

	Args:
		filterChoice (str): The filtering criteria to be used in the search.
			Possible options are:
				- 'Name' (Name): Filters records by contact name.
				- 'Cell phone' (Cellphone): Filters records by the contact's cell phone number.
				- 'Landline' (Landline): Filters records by the contact's landline number.
				- 'Email' (Email): Filters records by the contact's email address.
		keyword (str): The keyword to be used in the search. It can be a part of the name, phone number or email,
		depending on the filter chosen.

	Returns:
		list:A list of `ObjectContact` objects corresponding to the records found.
	"""

	query_map = {
		_('Name'): "SELECT * FROM contacts WHERE name LIKE ?",
		_('Cell phone'): "SELECT * FROM contacts WHERE cell LIKE ?",
		_('Landline'): "SELECT * FROM contacts WHERE landline LIKE ?",
		_('Email'): "SELECT * FROM contacts WHERE email LIKE ?",
	}
	query = query_map.get(filterChoice)
	if not query:
		# Lidar com erro ou retornar uma lista vazia
		return []
	with Section() as trans:
		trans.execute(query, ('%' + keyword + '%',))
		results = trans.fetchall()
	return convert_results(results)

def edit_record(ID, row):
	"""
	Function to update records in the database.

	Args:
		ID (int): The unique identifier of the record that will be updated.
		row (dict): A dictionary containing the new values ​​for the record.
			The dictionary keys must be:
				- 'name' (str): The contact's new name.
				- 'cell' (str): The contact's new cell phone number.
				- 'landline' (str): The contact's new landline number.
				- 'email' (str): The contact's new email address.
	"""

	with Section() as trans:
		trans.execute(
			"UPDATE contacts SET name =?, cell=?, landline=?, email=? WHERE id = ?",
			(row['name'], row['cell'], row['landline'], row['email'], ID)
		)
		trans.persist()


def delete(id):
	"""
	Function to remove a record from the database.

	Args:
		id (int): The unique identifier of the record to be removed.
	"""

	with Section() as trans:
		trans.execute("DELETE FROM contacts WHERE id=?", (id,))
		trans.persist()


def reset_record():
	"""
	Delete all records from the database.
	"""
	with Section() as trans:
		trans.execute("DELETE FROM contacts")
		trans.persist()


def import_csv_to_db(mypath):
	"""
	Imports data from a CSV file into the database.

	Args:
		mypath (str): The path to the CSV file that contains the data to be imported.

	Raises:
		FileNotFoundError: If the specified CSV file does not exist.
		csv.Error: If there is an error processing the CSV file.
	"""

	if not isinstance(mypath, str) or not os.path.isfile(mypath):
		raise FileNotFoundError(f"The file at {mypath} does not exist or is not a valid path.")

	with Section() as trans:
		try:
			with open(mypath, 'r', encoding="UTF-8") as file:
				sample = file.read(1024)
				file.seek(0)
				dialect = csv.Sniffer().sniff(sample)
				contents = csv.reader(file, dialect=dialect)
				insert_records = """
				INSERT INTO contacts(name, cell, landline, email)
				SELECT ?, ?, ?, ?
				WHERE NOT EXISTS (
					SELECT 1 FROM contacts WHERE name = ? AND cell = ? AND landline = ? AND email = ?
				)"""

				data_to_insert = [
					(name, cell, landline, email, name, cell, landline, email)
					for name, cell, landline, email in contents
				]
				trans.executemany(insert_records, data_to_insert)
			trans.persist()  # Persist only after successful execution
		except (FileNotFoundError, csv.Error, UnicodeDecodeError) as e:
			log.error(f"Error importing data: {str(e)}")
			raise  # Re-raise the exception after logging

def export_db_to_csv(mypath):
	try:
		with Section() as trans:
			trans.execute("SELECT * FROM contacts")
			rows = trans.fetchall() # Isso retorna uma lista de dicionários, como você já configurou.
			
# Use column names to extract values by excluding 'id'.
			# This is safe because dictionaries are hashable and have keys.
			cleaned_rows = [
				[row['name'], row['cell'], row['landline'], row['email']]
				for row in rows
			]
			
			with open(mypath, "w", newline="", encoding="UTF-8") as file:
				writer = csv.writer(file)
				writer.writerows(cleaned_rows)
	except Exception as e:
		log.error(f"Error export data to CSV: {str(e)}")
		# The exception must be relaunched to notify the interface
		raise

def count_records():
	"""
It counts the total number of records in the database safely.

Returns:
INT: The total number of records.
None: In case of error when accessing the database.
	"""
	try:
		with Section() as trans:
			if not trans.connected:
				return None
			
			trans.execute("SELECT COUNT(*) FROM contacts")
# Access the value of the dictionary by the 'Count (*)' key instead of the index [0].
			count = trans.cursor.fetchone()['COUNT(*)']
			return count
	except Exception as e:
		log.error(f"Erro ao contar registros no banco de dados: {e.__class__.__name__} - {e}")
		return None
