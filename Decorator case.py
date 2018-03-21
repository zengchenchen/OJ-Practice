def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def now():
    print('2015-3-25')


now1 = log(now)
now1()
