from types import *
import string
import sublime, sublime_plugin

TOGGLE_SETTINGS = []

class ToggleSettings(sublime_plugin.WindowCommand):
    def run(self):
        self._settings = []
        for name in TOGGLE_SETTINGS:
            value = self.window.active_view().settings().get(name)
            if isinstance(value, BooleanType):
                self._settings.append({'name': name, 'value': not value})
        if len(self._settings) > 0:
            self.window.show_quick_panel([_to_caption(setting) for setting in self._settings], self.on_done)
        else:
            sublime.status_message('ToggleSettings: None')

    def on_done(self, index):
        if index != -1:
            setting = self._settings[index]
            self.window.active_view().settings().set(setting['name'], setting['value'])
            sublime.status_message('ToggleSettings: {0[name]} -> {0[value]}'.format(setting))

    def is_enabled(self):
        return self.window.active_view() is not None

def _to_caption(setting):
    return 'Set {0}: {1}'.format(setting['value'], string.capwords(setting['name'].replace('_', ' ')))

def _load_settings():
    global TOGGLE_SETTINGS
    TOGGLE_SETTINGS = sublime.load_settings('ToggleSettings.sublime-settings').get('toggle_settings', [])

def plugin_loaded():
    _load_settings()
    sublime.load_settings('ToggleSettings.sublime-settings').add_on_change('load_settings', _load_settings)

if int(sublime.version()) < 3000:
    plugin_loaded()
