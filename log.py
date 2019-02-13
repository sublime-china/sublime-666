class Log():
    DEBUG = False

    @staticmethod
    def debug(msg):
        if Log.DEBUG:
            print('|||Sublime 666||| [debug]', msg)

    @staticmethod
    def info(msg):
        print('|||Sublime 666||| [info]', msg)

    @staticmethod
    def warning(msg):
        print('|||Sublime 666||| [warning]', msg)

    @staticmethod
    def error(msg):
        print('|||Sublime 666||| [error]', msg)
