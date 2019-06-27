# -*- coding: utf-8 -*-

from .libs import log, storage
import sublime


class S6Setting(object):
    def __init__(self):
        super(S6Setting, self).__init__()
        self._setting = storage.StorageSetting('sublime_666')

    def get_git_remote(self):
        remote = self._setting.get('git_remote', None)
        if remote is None:
            window = sublime.active_window()
            def on_done(remote):
                self.set_git_remote(remote)
            window.show_input_panel('git remote url:', '', on_done, None, None)
        return remote

    def set_git_remote(self, remote):
        self._setting.set('git_remote', remote)
        self._setting.save()
