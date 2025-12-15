- Replace custom sqlite311 library with newer sqlite3 (64-bit only)
- Remove old sqlite311 directory and its tests
- Refactor masked control imports to use wx.lib.masked and wx.tools.dbg
- Update csv.py to a newer implementation
- Add __main__.py for sqlite3 CLI support
- Fix import order and apply minor code cleanups across contactsManager addon

BREAKING CHANGE: This add-on is no longer compatible with 32-bit versions of NVDA.
