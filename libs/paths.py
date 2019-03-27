# -*- coding: utf-8 -*-

import sublime
import os


def get_file_path_cache(name):
    return os.path.join(sublime.cache_path(), 'User', '%s.cache' % name)


def get_setting_path_user(name):
    return os.path.join(sublime.packages_path(), 'User',
                        '%s.sublime-settings' % name)
