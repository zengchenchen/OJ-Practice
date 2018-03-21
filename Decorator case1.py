def log(func):
    def wrapper(x, y):
        print('call %s():' % func.__name__)
        return func(x)
    return wrapper


@log
def now(a):
    print('2015-3-25', a)


now('z', 1)
