# Changelog

This commit introduces support for 64-bit bundled libraries (lib64), including lib64 sqlite3/binaries. The code now dynamically selects between 'lib' and 'lib64' based on the IS64 flag.

Improvements to the GlobalPlugin dialog lifecycle include:

- Using `wx.CallAfter` for better event handling.
- Unifying `displayDialog` with destruction binding.
- Implementing safer `show`/`raise`/`restore` handling.

The add/edit form paste behavior has been enhanced to:

- Clean clipboard digits.
- Align and pad values to masked fields.
- Manage cursor placement more effectively.
- Tighten import error logging for missing masked libraries.

Internal `csv` and `masked` modules have been reformatted and tidied (style/whitespace, signature formatting).

Documentation has been updated in pt_BR, pt_PT, and uk to include:

- WhatsApp open feature.
- Keyboard notes.
- Layout fixes.

Additionally, some VSCode python analysis paths have been removed from settings, and `sqlLoader.py` and small ancillary updates (buildVars, readme) have been added.
