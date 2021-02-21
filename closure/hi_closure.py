# def foo():
#     msg = 'Hello world'

#     def bar():
#         return msg

#     return bar

# f = foo()
# print(f.__name__)
# print(f())
def foo(msg):

    def bar():
        return msg

    return bar

f_hi = foo('hi')
f_bye = foo('bye')
print(f_hi()) # 0x7fdcc2259550
print(f_bye()) # 0x7fdcc22595e0
