SublimeToggleSettings
=====================

A plugin for Sublime Text, toggle boolean type settings via the command palette.

Usage
-----

1. Click the *Preferences > Package Settings > ToggleSettings > Settings – User* menu entry

2. Add list of setting names to `ToggleSettings.sublime-settings` like this:

    ```json
    {
        "toggle_settings": ["fold_buttons", "trim_trailing_white_space_on_save"]
    }
    ```

    *Note: There are must be exists and boolean type settings.*

3. Run *Preferences: Toggle Settings – Current View* command via the command palette and select setting name to toggle it, enjoy :)
