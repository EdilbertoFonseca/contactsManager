# Changelog

Introduces multiple enhancements to contact handling:

- Directly open saved contacts in WhatsApp from the contact list.
- Perform a search when Enter is pressed in the search field.
- Intercept Ctrl+V on contact phone fields to paste only digits.

Details:

- Direct WhatsApp Opening (Contact List): Pressing Enter on a contact in the list now opens that contact directly in WhatsApp.
- Search Execution (Search Field): Pressing Enter in the search field now triggers the search action.

Clean Pasted Phone Input:

- Binds EVTCHARHOOK for cell and landline inputs.
- Adds `onPasteAndClean` to: Read the clipboard.
Strip non-digit characters using a regex.
- Set the cleaned value into the focused field (skipping default paste).
- Allows non-paste keys to be processed normally via `event.Skip()`.

Additionally updates `addonversion` to 2025.7.0 and replaces the `addonchangelog` text.
The changelog now includes notes about opening contacts in WhatsApp, enabling pasting into number fields, and the Enter key functionality.
