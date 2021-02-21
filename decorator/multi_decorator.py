import time
from functools import wraps

def mytimer(orig_func):
    @wraps(orig_func)
    def f(*args, **kwargs):
        t1 = time.perf_counter()
        orig_func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{orig_func.__name__} ran in {t2-t1} sec")
    return f


def mylogger(orig_func):
    @wraps(orig_func)
    def f(*args, **kwargs):
        print("start mylogger()")
        orig_func(*args, **kwargs)
        print("stop mylogger()")
    return f


@mylogger
@mytimer
def display(name, age):
    print(f"display {name}, {age}")


display("adnan", 28)
'''
start mylogger()
display adnan, 28
display ran in 1.4090000149735715e-05 sec
stop mylogger()
'''