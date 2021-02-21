from datetime import datetime
import time

def pre_datetime(func):
    def f(*args, **kwargs):
        if 'msg' in kwargs:
            kwargs['msg'] = f"{datetime.now()} | {kwargs['msg']}"
        func(*args, **kwargs)
    return f

@pre_datetime
def mylogger(msg):
    print(msg)

@pre_datetime
def yourlogger(msg, num):
    print(f"{msg} | {num}")

mylogger(msg="started")
time.sleep(2)
mylogger(msg="stopped")
yourlogger(msg="started",num=23)
time.sleep(2)
yourlogger(msg="stopped",num=44)