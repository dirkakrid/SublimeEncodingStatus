
import sublime
import sublime_plugin


class EncodingStatus(sublime_plugin.EventListener):
    '''Simply appends the current encoding to the status.'''

    def __init__(self):
        self.default_enc = None

    def on_activated(self, view):
        if view.is_loading():
            view.erase_status('encoding')
        else:
            self._set_encoding(view)

    def on_load(self, view):
        self._set_encoding(view)

    def on_post_save(self, view):
        self._set_encoding(view)

    def _set_encoding(self, view):
        enc = view.encoding()
        s = sublime.load_settings('Preferences.sublime-settings')
        if enc == 'Undefined':
            default_enc = s.get('default_encoding')
            view.set_status('encoding', '%s (Default)' % default_enc)
        else:
            fallback_enc = s.get('fallback_encoding')
            if enc == fallback_enc:
                view.set_status('encoding', '%s (Fallback)' % enc)
            else:
                view.set_status('encoding', enc)
