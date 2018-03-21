def log1(func):
    def wrapper(*args, **kw):
        print('begin call')
        func(*args, **kw)
        return print('end call')
    return wrapper


@log1
def now():
    print('try')


now()
