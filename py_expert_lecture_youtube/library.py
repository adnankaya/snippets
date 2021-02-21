import builtins
"""
#1.way
class Base:
    def foo(self):
        return self.bar()


old_bc = __build_class__


# def my_bc(*a, **kw):
#     print(f"my buildclass -> a:{a} kw:{kw}")
#     return old_bc(*a, **kw)


# we can use __build_class__ to ensure that
# bar method is exist/implemented by user.py
def my_bc(func, name, base=None, **kw):
    if base is Base:
        print("check if bar method is defined")
        if not hasattr(base,'bar'):
            raise NotImplementedError("bar() method has not been implemented")
    if base is not None:
        return old_bc(func, name, base, **kw)
    return old_bc(func, name, **kw)

builtins.__build_class__ = my_bc
"""

"""#2.way
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'Base' and not 'bar' in body:
            raise NotImplementedError("bad user! you must have bar() method")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

""" 

class Base():
    def foo(self):
        return self.bar()
    
    def __init_subclass__(cls):
        # TODO: add some features
        return super().__init_subclass__()