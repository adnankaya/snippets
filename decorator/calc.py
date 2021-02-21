import time


def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        rv = func(*args, **kwargs)
        after = time.time()
        print(f"Elapsed: {after-before}")
        return rv
    return f


@timer
def add(x, y=10):
    time.sleep(2)
    return x+y


@timer
def sub(x, y=10):
    time.sleep(2)
    return x-y


print(f"add(5): {add(5)}")
print(f"sub(15,20): {sub(15,20)}")
