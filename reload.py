# -*- coding: utf-8 -*-

import sys
import os
from imp import reload
from .libs import log, paths, storage
# log.enable()

dirname = os.path.split(os.path.dirname(__file__))[1]

all_modules = [
    'libs.log',
    'libs.paths',
    'libs.storage',
    'package_control_setting',
]


def reload_module():
    for module in all_modules:
        name = '%s.%s' % (dirname, module)
        reload(sys.modules[name])
    stop_thread(main_thread)


def plugin_loaded():
    log.debug('---------- plugin_loaded ----------')
    reload_module()
    start_thread()


def plugin_unloaded():
    log.debug('---------- plugin_unloaded ----------')
    stop_thread(main_thread)


import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    pyobj = ctypes.py_object(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, pyobj)
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def start_thread():
    log.debug('start thread')
    main_thread.start()


def stop_thread(thread):
    try:
        _async_raise(thread.ident, SystemExit)
        log.debug('stop thread')
    except:
        log.debug('stop thread failed')


TICK_TIME = 1


class Tick(threading.Thread):
    def run(self):
        while True:
            time.sleep(TICK_TIME)


main_thread = Tick()
