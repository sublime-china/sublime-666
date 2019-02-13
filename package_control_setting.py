import sublime
from .log import Log
#Log.DEBUG = True

CHANNELS_URL = 'http://www.miaoqiyuan.cn/products/proxy.php/https://packagecontrol.io/channel_v3.json'
ORIGIN_CHANNELS_URL = 'https://packagecontrol.io/channel_v3.json'
REPOSITORIES_URL = 'https://github.com/sublime-china'
SETTINGS_NAME = 'Package Control.sublime-settings'


def deal_setting(name):
    def decorator(func):
        def wrapper():
            s = sublime.load_settings(SETTINGS_NAME)
            params = s.get(name, None)
            if params != None:
                func(params)
                s.set(name, params)
                sublime.save_settings(SETTINGS_NAME)

        return wrapper

    return decorator


@deal_setting('channels')
def modify_channels(params):
    if ORIGIN_CHANNELS_URL in params:
        params.remove(ORIGIN_CHANNELS_URL)
    if CHANNELS_URL not in params:
        params.append(CHANNELS_URL)


@deal_setting('repositories')
def modify_repositories(params):
    if REPOSITORIES_URL not in params:
        params.append(REPOSITORIES_URL)


@deal_setting('channels')
def restore_channels(params):
    if CHANNELS_URL in params:
        params.remove(CHANNELS_URL)
    if ORIGIN_CHANNELS_URL not in params:
        params.append(ORIGIN_CHANNELS_URL)


@deal_setting('repositories')
def restore_repositories(params):
    if REPOSITORIES_URL in params:
        params.remove(REPOSITORIES_URL)


def plugin_unloaded():
    Log.debug('---------- plugin_unloaded ----------')
    restore_channels()
    restore_repositories()


def plugin_loaded():
    Log.debug('---------- plugin_loaded ----------')
    modify_channels()
    modify_repositories()
