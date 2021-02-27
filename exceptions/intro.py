a = 4
# print(a)) # SyntaxError: unmatched ')'
# b = '23' + 44 # TypeError: can only concatenate str (not "int") to str
# import somemodule # ModuleNotFoundError: No module named 'somemodule'
# a = c # NameError: name 'c' is not defined
# f = open('test.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
li = [1, 2]
# li.remove(5)  # ValueError: list.remove(x): x not in list
# li[19] # IndexError: list index out of range
d = {'name': 'adnan'}
# print(d['age']) # KeyError: 'age'
x = -11
# if x < 0:
#     raise Exception('x must be postivive')

y = 46
# AssertionError raises
# assert(y <= 44), 'y must be lower than 44 or equal'

# a = 5 / 0  # ZeroDivisionError: division by zero

# try:
#     a = 100/0
# except:
#     print("[my error message]: you should not try to divide by 0")


try:
    a = 5 / 1  # 0
    b = 'adnan' + "28"  # remove quotes
except ZeroDivisionError as zde:
    print(f"zde: {zde}")
except TypeError as te:
    print(f"te: {te}")
else:
    print("Everything is fine")
finally:  # works in every condition
    print("finally you did!..")

# define your own error class


class ValueTooBigError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, msg, val):
        self.msg = msg
        self.val = val


def test_func(x):
    if x > 1_000_000:
        raise ValueTooBigError("value can not be greater than 1 million")
    if x < 0:
        raise ValueTooSmallError("too small", x)


try:
    test_func(-2_000_000)
except ValueTooBigError as vtbe:
    print(f"vtbe: {vtbe}")
except ValueTooSmallError as vtse:
    print(vtse.msg, vtse.val)
