# Contact Manager for NVDA

* **Author**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Creation Date**: 04/11/2024
* **License**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introduction

Welcome to the Contact Manager for NVDA! This add-on is specially designed to help visually impaired individuals manage their contact lists with greater ease and efficiency. With this add-on, you can add, edit, and delete contacts, as well as search for names and contact information quickly and easily. Additionally, we offer the ability to export and import your contact list, allowing you to share it. The Contact Manager for NVDA is user-friendly and provides an intuitive interface, making it the ideal choice for those who need efficient contact list management.

## Installation

Here are the step-by-step instructions to install the Contact Manager for NVDA:

1. **Download the add-on installation file**: Obtain the file from the Add-on Store or the official [Contact Manager page](https://github.com/EdilbertoFonseca/contactManager).
   **Note**: If the add-on is downloaded from the store, the installation will occur automatically. Otherwise, follow the instructions below.
2. **Install the add-on**: Press Enter on the downloaded add-on file.
3. **Follow the on-screen instructions**: Complete the installation as directed.
4. **Restart NVDA**: Restarting is required to activate the add-on.
5. **Verify the installation**: Press `NVDA+N` to open the NVDA menu, navigate to "Tools," and check if the Contact Manager add-on is listed.

Now you're ready to use the Contact Manager for NVDA and save your contacts directly from NVDA.

## Settings

In the NVDA menu, Preferences > Settings > Contact Manager for NVDA, you can configure the following options:

1. Add masks for phone fields.
   This option adds a mask using the hash symbol `#` to format phone numbers. By default, mobile and landline fields are formatted for Brazil.
2. Show option to delete the entire calendar, checkbox checked `Alt+t`.
   When enabled, it allows deleting all the content of the calendar.
3. Show CSV file import button, checkbox checked `Alt+I`.
   Allows importing CSV files.
   Note: All fields must be compatible with the Contact Manager.
4. Show CSV file export button, checkbox checked `Alt+X`.
   Saves all calendar contacts to a CSV file.
5. Agenda file path.
   Allows selecting or adding a directory different from the default one for the database.

## Usage

You can access the Contact Manager for NVDA in two ways:

1. By shortcut, `Windows+Alt+L`;
2. Through the NVDA menu: `NVDA+N` > Tools > Contact Manager.

You will have access to the add-on's main window. In this window, you can register, edit, remove, and search contacts. It also includes options to import CSV, export CSV, and delete the entire calendar. These three options are enabled by default but can be disabled in the settings panel.

### Registering a new contact

To register a new contact:

1. Access the Contact Manager: NVDA menu > Tools > Contact Manager, or by shortcut `Windows+Alt+L`;
2. In the Contact List window, press `Alt+N` to add a new contact;
3. In the New Contact window, fill in all the fields and press `Alt+O` to save or `Alt+C` to exit without saving.
   > **Note**: To navigate between fields, press the "Enter" key. You can also use the "Tab" key, but it may behave unpredictably due to an unresolved issue.

### Editing a contact

To edit a contact:

1. Select a contact from the list;
2. Press `Alt+E` or use the `F2` key.

The edit window will open with the focus on the name field. Edit the fields and press `Alt+O` to save changes or `Alt+C` to cancel.
> **Note**: To navigate between fields, press the "Enter" key. You can also use the "Tab" key, but it may behave unpredictably due to an unresolved issue.

### Searching

In the Contact List window, use the search field to locate a specific contact.
You can search by the following fields:

* Name;
* Mobile;
* Landline;
* Email.

After selecting the field, enter the search term and press the shortcut `Alt+P` to display the results in the list. If no results are found, a message will appear stating that the item was not found. To refresh, use the shortcut `Alt+A` or the `F5` key.

## Tips and Shortcuts

### Contact List Window

* **Search Button**: `Alt+P`
* **Edit Button**: `Alt+E` (also accessible with `F2`)
* **New Button**: `Alt+N`
* **Remove Button**: `Alt+R` (also accessible with the `Delete` key)
* **Refresh Button**: `Alt+A` (also accessible with `F5`)
* **Import CSV Button**: `Alt+I`
* **Export CSV Button**: `Alt+X`
* **Delete All Records Button**: `Alt+T`
* **Exit Button**: `Alt+S`

### New Contact and Edit Windows

* **Confirm Operations**: `Alt+O`
* **Cancel Button**: `Alt+C`

> All windows in the Contact Manager for NVDA can be closed using the `Esc` or `Alt+F4` keys.

## Acknowledgments

This add-on was inspired by the agenda created by Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com>, and Ângelo Abrantes <ampa4374@gmail.com>.
