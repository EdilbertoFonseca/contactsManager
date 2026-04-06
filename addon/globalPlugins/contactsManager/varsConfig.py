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

# Retrieve the country code list
countryCode = [
	("244", "Angola"),
	("376", "Andorra"),
	("54", "Argentina"),
	("43", "Áustria"),
	("994", "Azerbaijão"),
	("1-242", "Bahamas"),
	("973", "Bahrein"),
	("880", "Bangladesh"),
	("1-246", "Barbados"),
	("375", "Bielorrússia"),
	("501", "Belize"),
	("591", "Bolívia"),
	("387", "Bósnia e Herzegovina"),
	("267", "Botsuana"),
	("55", "Brasil"),
	("673", "Brunei"),
	("359", "Bulgária"),
	("226", "Burkina Faso"),
	("257", "Burundi"),
	("855", "Camboja"),
	("237", "Camarões"),
	("1", "Canadá"),
	("974", "Catar"),
	("97", "Cazaquistão"),
	("235", "Chade"),
	("56", "Chile"),
	("86", "China"),
	("357", "Chipre"),
	("57", "Colômbia"),
	("269", "Comores"),
	("242", "Congo"),
	("850", "Coreia do Norte"),
	("82", "Coreia do Sul"),
	("506", "Costa Rica"),
	("225", "Costa do Marfim"),
	("385", "Croácia"),
	("53", "Cuba"),
	("599", "Curaçau"),
	("45", "Dinamarca"),
	("253", "Djibuti"),
	("1-767", "Dominica"),
	("593", "Equador"),
	("20", "Egito"),
	("503", "El Salvador"),
	("971", "Emirados Árabes Unidos"),
	("421", "Eslováquia"),
	("386", "Eslovênia"),
	("34", "Espanha"),
	("1", "Estados Unidos"),
	("372", "Estônia"),
	("251", "Etiópia"),
	("679", "Fiji"),
	("63", "Filipinas"),
	("358", "Finlândia"),
	("33", "França"),
	("220", "Gâmbia"),
	("233", "Gana"),
	("995", "Geórgia"),
	("350", "Gibraltar"),
	("30", "Grécia"),
	("299", "Groenlândia"),
	("1-473", "Granada"),
	("502", "Guatemala"),
	("245", "Guiné-Bissau"),
	("592", "Guiana"),
	("509", "Haiti"),
	("504", "Honduras"),
	("852", "Hong Kong"),
	("36", "Hungria"),
	("91", "Índia"),
	("62", "Indonésia"),
	("98", "Irã"),
	("964", "Iraque"),
	("353", "Irlanda"),
	("354", "Islândia"),
	("972", "Israel"),
	("39", "Itália"),
	("1-876", "Jamaica"),
	("81", "Japão"),
	("962", "Jordânia"),
	("254", "Quênia"),
	("996", "Quirguistão"),
	("856", "Laos"),
	("371", "Letônia"),
	("961", "Líbano"),
	("266", "Lesoto"),
	("231", "Libéria"),
	("218", "Líbia"),
	("423", "Liechtenstein"),
	("370", "Lituânia"),
	("352", "Luxemburgo"),
	("853", "Macau"),
	("261", "Madagascar"),
	("60", "Malásia"),
	("265", "Malaui"),
	("960", "Maldivas"),
	("356", "Malta"),
	("212", "Marrocos"),
	("230", "Maurício"),
	("52", "México"),
	("373", "Moldávia"),
	("377", "Mônaco"),
	("976", "Mongólia"),
	("382", "Montenegro"),
	("258", "Moçambique"),
	("95", "Myanmar"),
	("264", "Namíbia"),
	("977", "Nepal"),
	("505", "Nicarágua"),
	("234", "Nigéria"),
	("47", "Noruega"),
	("64", "Nova Zelândia"),
	("968", "Omã"),
	("92", "Paquistão"),
	("970", "Palestina"),
	("507", "Panamá"),
	("675", "Papua-Nova Guiné"),
	("595", "Paraguai"),
	("31", "Países Baixos"),
	("51", "Peru"),
	("48", "Polônia"),
	("351", "Portugal"),
	("974", "Catar"),
	("44", "Reino Unido"),
	("236", "República Centro-Africana"),
	("420", "República Tcheca"),
	("40", "Romênia"),
	("99", "Rússia"),
	("250", "Ruanda"),
	("685", "Samoa"),
	("378", "San Marino"),
	("239", "São Tomé e Príncipe"),
	("221", "Senegal"),
	("381", "Sérvia"),
	("65", "Cingapura"),
	("963", "Síria"),
	("252", "Somália"),
	("94", "Sri Lanka"),
	("249", "Sudão"),
	("597", "Suriname"),
	("46", "Suécia"),
	("41", "Suíça"),
	("66", "Tailândia"),
	("255", "Tanzânia"),
	("66", "Tailândia"),
	("670", "Timor-Leste"),
	("228", "Togo"),
	("676", "Tonga"),
	("1-868", "Trinidad e Tobago"),
	("216", "Tunísia"),
	("90", "Turquia"),
	("993", "Turcomenistão"),
	("256", "Uganda"),
	("380", "Ucrânia"),
	("598", "Uruguai"),
	("998", "Uzbequistão"),
	("678", "Vanuatu"),
	("58", "Venezuela"),
	("84", "Vietnã"),
	("260", "Zâmbia"),
	("263", "Zimbábue"),
]

def initConfiguration():
	"""
	Initializes the configuration specification for the Contacts Manager for NVDA add-on.
	"""
	try:
		confspec = {
			"countryCode": """string(default="55")""",
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
