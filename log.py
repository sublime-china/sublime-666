class Log():
    DEBUG = False

    @staticmethod
    def debug(msg):
        if Log.DEBUG:
            print('[s666-debug]', msg)

    @staticmethod
    def info(msg):
        print('[s666-info]', msg)

    @staticmethod
    def warning(msg):
        print('[s666-warning]', msg)

    @staticmethod
    def error(msg):
        print('[s666-error]', msg)
