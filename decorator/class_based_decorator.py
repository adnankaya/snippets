
class MyDecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Added functionality for your {self.func.__name__} method")
        self.func(*args, **kwargs)

@MyDecoratorClass
def myfunc(msg):
    print(f"myfunc() worked with {msg}")


myfunc("hi")
myfunc("bye")