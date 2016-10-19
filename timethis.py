# coding: utf-8

def timethis(func):
    import time
    import functools
    import inspect
    import sys
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('--start', sys._getframe().f_code.co_name, '--')
        start = time.time()
        func(*args,**kwargs)
        elapsed_time = time.time() - start
        print(("elapsed_time:{0:.3f}".format(elapsed_time)), "[sec]")
        print('--end--')
    return wrapper
