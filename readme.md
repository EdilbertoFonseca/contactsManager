# Contact Manager for NVDA

* **Author**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Creation Date**: 04/11/2024
* **License**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introduction

Welcome to the Contact Manager add-on for NVDA! This is a plug-in specially developed to assist visually impaired users in managing their contact list with greater ease and efficiency. With this add-on, you can add, edit, and delete contacts, as well as quickly and easily search for names and contact information. Additionally, we also provide the ability to export and import your contact list, so you can share it. The Contact Manager for NVDA is user-friendly and features an intuitive interface, making it the ideal choice for anyone needing to efficiently manage their contact list.

## Installation

Here are the step-by-step instructions to install the Contact Manager for NVDA:

1. **Download the add-on installation file**: Get the file from the Add-ons Store or from the official [Contact Manager page](https://github.com/EdilbertoFonseca/contactManager).
   **Note**: If the add-on is downloaded from the store, installation will occur automatically. Otherwise, follow the instructions below.
2. **Install the add-on**: Press Enter on the downloaded add-on file.
3. **Follow the on-screen instructions**: Complete the installation as directed.
4. **Restart NVDA**: A restart is necessary to activate the add-on.
5. **Check the installation**: Press `NVDA+N` to open the NVDA menu, go to "Tools," and verify that the Contact Manager add-on is listed.

Now you're ready to use the Contact Manager for NVDA and save your contacts directly from NVDA.

## Settings

In the NVDA Preferences menu, under Settings..., in the Contact Manager for NVDA option, you can configure the following options:

1. Add mask for phone fields.
   This option adds a mask using the `#` symbol to format phone numbers. By default, the mobile and landline fields are formatted for Brazil.
2. Display the option to delete the entire agenda, checkbox unchecked. `Alt+T`.
   When enabled, it allows you to delete all content in the agenda.
3. Display Import CSV file, checkbox unchecked. `Alt+I`.
   Allows importing CSV files.
   Note: All fields must be compatible with the Contact Manager.
4. Display Export CSV file, checkbox unchecked. `Alt+X`.
   Saves all contacts from the agenda in a CSV file.
5. Agenda file path.
   Allows you to select or add a different directory from the default for the database.

## Usage

You can access the Contact Manager for NVDA in two ways:

1. Using the shortcut `Windows+Alt+L`;
2. Through the NVDA menu `NVDA+N`, Tools, Contact Manager.

You will have access to the main window of the add-on. In this window, you can register, edit, remove, and search for contacts. It also includes options to import CSV, export CSV, and delete the entire agenda. These three options are enabled by default and can be disabled in the settings panel.

### Registering a New Contact

To register a new contact:

1. Access the Contact Manager, NVDA menu, Tools, Contact Manager, Contact Manager, or use the shortcut `Windows+Alt+L`;
2. In the Contact List window, press `Alt+N` to add a new contact.
3. In the New Contact window, fill in all the fields and press `Alt+O` to save, or `Alt+C` to exit without saving;
   >Note: To navigate between fields, simply press the "Enter" key. You can also use the "Tab" key, but it may exhibit unpredictable behavior due to an issue I have yet to identify.

### Editing a Contact

To edit a contact:

1. Select a contact from the list;
2. Press `Alt+E` or use the `F2` key.

The edit window will open, focused on the name field. Simply edit and press `Alt+O` to save the changes or `Alt+C` to cancel.
>Note: To navigate between fields, simply press the "Enter" key. You can also use the "Tab" key, but it may exhibit unpredictable behavior due to an issue I have yet to identify.

### Searching

In the Contact List window, you can use the search field to locate a specific contact.
You can search by the following fields:

* Name;
* Mobile;
* Landline;
* E-mail.

After selecting the field, enter the search term and press the shortcut `Alt+P` to display the results in the list. If no results are found, a message will appear indicating that the item was not found. To refresh, use the shortcut `Alt+A` or the `F5` key.

## Tips and Shortcuts

### Contact List Window

* **Search Button**: `Alt+P`
* **Edit Button**: `Alt+E` (can also use the `F2` key)
* **New Button**: `Alt+N`
* **Remove Button**: `Alt+R` (can also use the `Delete` key)
* **Refresh Button**: `Alt+A` (can also use the `F5` key)
* **Import CSV Button**: `Alt+I`
* **Export CSV Button**: `Alt+X`
* **Delete All Records Button**: `Alt+T`
* **Exit Button**: `Alt+S`

### New Contact and Edit Window

* **Confirm operations**: `Alt+O`
* **Cancel Button**: `Alt+C`

>All windows of the Contact Manager for NVDA add-on can be closed with the `Esc` key or `Alt+F4`.

## Acknowledgments

This add-on was inspired by the agenda created by Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com>, and Ângelo Abrantes <ampa4374@gmail.com>.
