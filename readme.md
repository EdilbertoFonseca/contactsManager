# Contact Manager for NVDA

- **Author**: Edilberto Fonseca (<edilberto.fonseca@outlook.com>)  
- **Creation Date**: 2024-04-11  
- **License**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introduction

Welcome to the **Contact Manager for NVDA**!

This add-on was developed to help visually impaired users manage their contact list in a practical, accessible, and efficient way. With this tool, you can:

- Add, edit, and delete contacts;
- Search contact names and information quickly;
- Import and export contacts in CSV format, making backups and sharing easier.

The Contact Manager provides a simple and intuitive interface, making it a valuable tool for those who need an accessible way to manage their contacts within NVDA.

## Installation

1. In NVDA, open the **Tools** menu and go to the **Add-on Store**.
2. Under the **Available Add-ons** tab, use the **Search** field.
3. Type `contactsManager`. When the result appears, press **Enter** or click **Apply**, then choose **Install**.
4. Restart NVDA to complete the installation.

The add-on is now ready to use.

When you select a contact in the list, their details will be shown in a read-only text box. You can navigate the list using the first letter of the contact’s name.

## Settings

Access the settings panel from:  
**NVDA Menu > Preferences > Settings... > Contact Manager for NVDA**

The following options are available:

1. **Add phone field masks**  
   Applies a mask using the `#` symbol to format phone numbers. The default format is based on Brazilian phone standards.

2. **Show option to delete all contacts** (`Alt+T`)  
   When enabled, allows you to delete all contacts from the address book at once.

3. **Show button to import CSV file** (`Alt+I`)  
   Enables importing contacts from a CSV file.  
   > Note: The fields in the CSV must match the structure used by the Contact Manager.

4. **Show button to export CSV file** (`Alt+X`)  
   Exports all contacts to a CSV file.

5. **Contacts file directory**  
   Lets you set a custom folder for the contact database, different from the default.

## Usage

You can open the Contact Manager in two ways:

1. Keyboard shortcut: `Windows+Alt+L`  
2. NVDA Menu: `NVDA+N > Tools > Contact Manager > Contact Manager`

In the main window, you can:

- Add, edit, and delete contacts;
- Search for specific contacts;
- Import and export CSV files;
- Delete all records in the contact list (optional).

The import, export, and delete-all options are enabled by default, but can be disabled in the settings panel.

### Adding a New Contact

1. Open the Contact Manager (`Windows+Alt+L` or through the NVDA menu).
2. In the contact list window, press `Alt+N` to add a new contact.
3. Fill out the fields and press `Alt+O` to save, or `Alt+C` to cancel.

> **Note:**  
> To move between fields, it is recommended to use the `Enter` key. While the `Tab` key may work, it might behave unpredictably due to an unresolved issue.

### Editing a Contact

1. Select a contact from the list.
2. Press `Alt+E` or `F2` to open the edit window.
3. After making changes, press `Alt+O` to save or `Alt+C` to cancel.

> **Note:**  
> Navigation between fields works the same as in the new contact window.

### Search

In the contact list window:

1. Use the search field to find a contact by:
   - Name
   - Mobile phone
   - Landline
   - Email
2. After entering your search term, press `Alt+P` to display the results.
3. To refresh the list and clear the search, press `Alt+A` or `F5`.

If the contact is not found, a message will inform you that no results were found.

## Tips and Shortcuts

### Contact List Window

| Action                      | Shortcut            |
|-----------------------------|---------------------|
| Search                      | `Alt+P`             |
| Edit                        | `Alt+E` or `F2`     |
| New contact                 | `Alt+N`             |
| Remove contact              | `Alt+R` or `Delete` |
| Refresh list                | `Alt+A` or `F5`     |
| Import CSV                  | `Alt+I`             |
| Export CSV                  | `Alt+X`             |
| Delete all contacts         | `Alt+T`             |
| Exit                        | `Alt+S`             |

> **Important:**  
> To **edit** or **remove** a contact, it must be **selected in the list** beforehand.  
> If no contact is selected, a message will be displayed stating that **no contact was selected**.

### New Contact / Edit Contact Window

| Action          | Shortcut  |
|------------------|-----------|
| Confirm          | `Alt+O`   |
| Cancel           | `Alt+C`   |

> **Tip:**  
> All Contact Manager windows can be closed using `Esc` or `Alt+F4`.

## Acknowledgements

This add-on was inspired by the contact manager originally created by:

- Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)  
- Rui Fontes (<rui.fontes@tiflotecnia.com>)  
- Ângelo Abrantes (<ampa4374@gmail.com>)
