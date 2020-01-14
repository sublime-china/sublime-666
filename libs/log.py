# coding:utf-8

__DEBUG = False
LOG_PREFIX = "Sublime 666"


def enable():
    global __DEBUG
    __DEBUG = True


def debug(*msg):
    if __DEBUG:
        print("[%s %s]" % (LOG_PREFIX, "Debug"), " ".join([str(x) for x in msg]))


def info(*msg):
    print("[%s %s]" % (LOG_PREFIX, "Info"), " ".join([str(x) for x in msg]))


def warning(*msg):
    print("[%s %s]" % (LOG_PREFIX, "Warning"), " ".join([str(x) for x in msg]))


def error(*msg):
    print("[%s %s]" % (LOG_PREFIX, "Error"), " ".join([str(x) for x in msg]))
