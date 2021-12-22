

from functools import wraps


def logger(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logger
def foo(x):
    '''multiply given parameter itself'''
    return x*x

print(foo.__name__)
print(foo.__doc__)
print(foo(5))
print('_'*30)
# ======================== wraps ======================================
def logging(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logging
def bar(x):
    '''multiply given parameter itself'''
    return x*x

print(bar.__name__)
print(bar.__doc__)
print(bar(5))

"""
with_logging                        # we lost name of foo function
None                                # we lost docstring of foo function
foo was called
25
______________________________
bar                                 # we keep name of bar function
multiply given parameter itself     # we keep docstring of bar function
bar was called
25

# NOTE ################################################
If using a decorator always meant losing this information about a function, it would be a serious problem. 
That's why we have functools.wraps. 
This takes a function used in a decorator and 
    adds the functionality of copying over the function name, docstring, arguments list, etc. 
    And since wraps is itself a decorator,
"""

"""
# NOTE
@functools.wraps(f)
def g():
    pass

Is an alias for  `g = functools.update_wrapper(g, f)` 
It does exactly three things:

1. it copies the __module__, __name__, __qualname__, __doc__, and __annotations__ attributes of f on g. 
    This default list is in WRAPPER_ASSIGNMENTS, you can see it in the functools source.
2. it updates the __dict__ of g with all elements from f.__dict__. (see WRAPPER_UPDATES in the source)
3. it sets a new __wrapped__=f attribute on g
"""

