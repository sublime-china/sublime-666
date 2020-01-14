# -*- coding: utf-8 -*-

import sublime
import os
from .s6_setting import S6Setting
from .cmd import run_command
from .libs import log
import time

user_path = os.path.join(sublime.packages_path(), 'User')
user_path_git = os.path.join(user_path, '.git')

class SettingSync(S6Setting):
    def __init__(self):
        super(SettingSync, self).__init__()

    def git_init(self):
        run_command('cd {} && git init'.format(user_path))

    def add_remote(self):
        remote = self.get_git_remote()
        run_command('cd {} && git remote add origin {}'.format(user_path, remote))

    def git_commit(self):
        run_command('cd {} && git add . && git commit -am \'update at {}\''.format(user_path, time.ctime()))
        

def get_setting_sync():
    return SettingSync()

def plugin_loaded():
    # [comment by Floyda] sublime_666
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    if not os.path.exists(user_path_git):
        s = get_setting_sync()
        s.git_init()
        s.add_remote()
