class BaseException(Exception):
    pass


class LevelException(BaseException):
    print('Low level')


class AccessException(BaseException):
    print('Access')
