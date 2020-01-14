# -*- coding: utf-8 -*-

import subprocess


def wrap_func(func, args=None):
    if func is None:
        return
    if args:
        func(args)
    else:
        func()


def run_command(cmd, success=None, failure=None):
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    msg, err = p.communicate()
    if err is not "":
        return wrap_func(failure)
    else:
        return wrap_func(success, msg)
