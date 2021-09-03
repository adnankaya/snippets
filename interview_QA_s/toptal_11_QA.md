1. What will be the output of the code below? Explain your answer.
```bash
In [1]: def extend_list(val, li=[]):
   ...:     li.append(val)
   ...:     return li
   ...: 

In [2]: li1 = extend_list(10)

In [3]: li2 = extend_list(123, [])

In [4]: li3 = extend_list('a')

In [5]: li1
Out[5]: [10, 'a']

In [6]: li2
Out[6]: [123]

In [7]: li3
Out[7]: [10, 'a']

```
How would you modify the definition of extendList to produce the presumably desired behavior?
```bash
def extend_list(val, li=None):
    ...:     if li is None:
    ...:         li = []
    ...:     li.append(val)
    ...:     return li
    ...: 

In [1]: li1 = extend_list(10)

In [2]: li2 = extend_list(123,[])

In [3]: li3 = extend_list('a')

In [4]: li1
Out[4]: [10]

In [5]: li2
Out[5]: [123]

In [6]: li3
Out[6]: ['a']
```
2. What will be output of the code below
```bash
In [1]: def multipliers():
    ...:     return [lambda x: i*x for i in range(4)]
    ...: 

In [2]: [func(2) for func in multipliers()]
Out[2]: [6, 6, 6, 6] # unecpected result!!

In [3]: multipliers()
Out[3]: 
[<function __main__.multipliers.<locals>.<listcomp>.<lambda>(x)>,
 <function __main__.multipliers.<locals>.<listcomp>.<lambda>(x)>,
 <function __main__.multipliers.<locals>.<listcomp>.<lambda>(x)>,
 <function __main__.multipliers.<locals>.<listcomp>.<lambda>(x)>]

```
How would you modify the definiton of multipliers to produce presumably desired behaviour.
```bash
# 1. would be using generator
In [1]: def multipliers():
   ...:     for i in range(4):
   ...:         yield lambda x: i*x
   ...: 

In [2]: [func(2) for func in multipliers()]
Out[2]: [0, 2, 4, 6]

# 2. creating closures
In [3]: [lambda x, i=i: i*x for i in range(4)]
Out[3]: 
[<function __main__.<listcomp>.<lambda>(x, i=0)>,
 <function __main__.<listcomp>.<lambda>(x, i=1)>,
 <function __main__.<listcomp>.<lambda>(x, i=2)>,
 <function __main__.<listcomp>.<lambda>(x, i=3)>]

In [4]: funclist = [lambda x, i=i: i*x for i in range(4)]

In [5]: [f(2) for f in funclist]
Out[5]: [0, 2, 4, 6]

# 3. using partials
In [1]: from functools import partial
   ...: from operator import mul

In [2]: [partial(mul, i) for i in range(4)]
Out[2]: 
[functools.partial(<built-in function mul>, 0),
 functools.partial(<built-in function mul>, 1),
 functools.partial(<built-in function mul>, 2),
 functools.partial(<built-in function mul>, 3)]

In [3]: funclist = [partial(mul, i) for i in range(4)]

In [4]: [f(2) for f in funclist]
Out[4]: [0, 2, 4, 6]
# 4. using comprehension to create a generator
In [1]: funclist = (lambda x: i*x for i in range(4))

In [2]: funclist
Out[2]: <generator object <genexpr> at 0x7ff74a43f120>

In [3]: [func(2) for func in funclist]
Out[3]: [0, 2, 4, 6]

```
- **The reason is list comprehension has the same references**
```bash
In [1]: funclist = (lambda x: i*x for i in range(4))
# All of these are DIFFERENT reference
In [2]: [id(f(2)) for f in funclist]
Out[2]: [9788576, 9788640, 9788704, 9788768]

In [3]: funclist = [lambda x: i*x for i in range(4)]
# All of these are the SAME reference
In [4]: [id(f(2)) for f in funclist]
Out[4]: [9788768, 9788768, 9788768, 9788768]
```
3. What will be output of the code below
```python
class Parent(object):
    x = 1
class Child1(Parent)
    pass
class Child2(Parent)
    pass

id(Parent.x), id(Child1.x), id(Child2.x)
# (9788608, 9788608, 9788608)
Child1.x = 2 # Child1.x -> reference is changed!!!
# id(Parent.x), id(Child1.x), id(Child2.x)
(9788608, 9788640, 9788608)
Parent.x = 3
# id(Parent.x), id(Child1.x), id(Child2.x)
(9788672, 9788640, 9788672)

# id() returns the object’s memory address.
# is returns True if and only if two objects have the same memory address.


print(Parent.x, Child1.x, Child2.x)
# 1, 1, 1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
# 1, 2, 1
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
# 3, 2, 3
```
- if any of its child classes overrides that value (for example, when we execute the statement Child1.x = 2), then the value is changed in that child only. That’s why the second print statement outputs 1 2 1.
- if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), that change is reflected also by any children that have not yet overridden the value (which in this case would be Child2). That’s why the third print statement outputs 3 2 3.
- The key to the answer is that, in Python, class variables are internally handled as dictionaries. 
-  If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found 
- (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs).

4. What would be the output of this code in Python2
```bash
>>> def div1(x, y):
...     print '%s / %s = %s' % (x,y, x/y )
... 
>>> def div2(x, y):
...     print '%s // %s = %s' % (x,y, x//y )
... 
>>> div1(5, 2)
5 / 2 = 2
>>> div1(5. , 2)
5.0 / 2 = 2.5
>>> div2(5, 2)
5 // 2 = 2
>>> div2(5. , 2)
5.0 // 2 = 2.0
>>> div2(5. , 2.)
5.0 // 2.0 = 2.0

```
5. What would be the output of this code?
```bash
In [1]: lx = []

In [2]: li = [ lx ] * 5 # equals [ [] ] *5
# above it simply creates a list of 5 lists.
# but did NOT create a list containing 5 distinct lists
In [3]: li
Out[3]: [[], [], [], [], []]
# in li, all of 5 elements have the same REFERENCE
In [4]: li[0].append(11)

In [5]: li
Out[5]: [[11], [11], [11], [11], [11]]

In [6]: li[1].append(44)

In [7]: li
Out[7]: [[11, 44], [11, 44], [11, 44], [11, 44], [11, 44]]

In [8]: li.append(9)

In [9]: li
Out[9]: [[11, 44], [11, 44], [11, 44], [11, 44], [11, 44], 9]

```

6.  What would be the output of this code?
```bash
In [1]: li = ['a', 'b', 'c']

In [2]: li[10:]
Out[2]: []

In [3]: li[10]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-3-f201d77b98ad> in <module>
----> 1 li[10]

IndexError: list index out of range
```
7.  Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
(a) even numbers, and
(b) from elements in the original list that had even indices

For example, if list[2] contains a value that is even, that value should be included in the new list, since it is also at an even index (i.e., 2) in the original list. However, if list[3] contains an even number, that number should not be included in the new list since it is at an odd index (i.e., 3) in the original list.
```bash
In [1]: def foo(N):
   ...:     return [i for i in N[::2] if i%2 == 0]
   ...: 
   ...: 

In [2]: foo(t)
Out[2]: [10, 18, 78]
```
8. How would you list the functions of a module?
```python
import some_module
dir(some_module)
```
9. What would be the output of this ?
```bash
In [1]: class DefaultDict(dict):
    ...:   def __missing__(self, key):
    ...:     return []
    ...: 

In [2]: d = DefaultDict()

In [3]: d['123']  = 123

In [4]: d
Out[4]: {'123': 123}

In [5]: d['a']
Out[5]: []

```
---

### Hands-on

```bash
In [9]: t
Out[9]: [1, 3, 5, 8, 10, 13, 18, 36, 78]

In [10]: t[:] # creates a list which have new reference
Out[10]: [1, 3, 5, 8, 10, 13, 18, 36, 78]

In [11]: id(t)
Out[11]: 139681936456384

In [12]: id(t[:])
Out[12]: 139681935893184

In [13]: id(t) == id(t[:])
Out[13]: False

In [14]: t
Out[14]: [1, 3, 5, 8, 10, 13, 18, 36, 78]

In [15]: t[:3] # start from index 0 to 3(not included)
Out[15]: [1, 3, 5]

In [16]: t[0:3] # start from index 0 to 3(not included)
Out[16]: [1, 3, 5]

In [17]: t[-1:3] # step is 1 as default
Out[17]: []

In [18]: t[-1:-4] # step is 1 as default
Out[18]: []

In [19]: t[-1:-4:-1] # step is -1 as we defined
Out[19]: [78, 36, 18]

In [20]: t
Out[20]: [1, 3, 5, 8, 10, 13, 18, 36, 78]

In [21]: t[::2] # start from index 0 to end(included), step is 2 as we defined
Out[21]: [1, 5, 10, 18, 78]

In [22]: t[0:8:2] # from index 0 to index 8(not included)
Out[22]: [1, 5, 10, 18]

In [23]: t[0:9:2] # from index 0 to index 9(actually we dont have index 9), step is 2 as we defined
Out[23]: [1, 5, 10, 18, 78]

In [24]: t[0:19:2] # we dont have index 19, but it works!
Out[24]: [1, 5, 10, 18, 78]

In [25]: t[9:19:2] # we dont have index 9,19, it works and return empty list.
Out[25]: []

In [26]: id([]) is id([]) # both have different references
Out[26]: False

In [27]: id([]) == id([])
Out[27]: True
In [28]: id([]) , id([])
Out[28]: (139681935521920, 139681935521920)
#########################################################################################
In []: id([])
Out[]: 140700055309504

In []: id([]), id([])
Out[]: (140700055156736, 140700055156736) # same line same reference

In []: id([]), id([]), id([])
Out[]: (140700055936704, 140700055936704, 140700055936704) # same line same reference
########################################################################################
In [29]: li1 = []

In [30]: li2 = []

In [31]: id(li1) , id(li2)
Out[31]: (139681936639168, 139681936792128) # these references are DIFFERENT

In [32]: id(li1) is id(li2) # different references
Out[32]: False

In [33]: id(li1) == id(li2) # different references are not equal too
Out[33]: False

In [34]: id('a') is id('a') # different references
Out[34]: False

In [35]: id('a') == id('a')
Out[35]: True

In [36]: id(123) == id(123)
Out[36]: True

In [37]: id(123) is id(123)
Out[37]: False

In [38]: x = 2

In [39]: y = 3

In [40]: z = 2

In [41]: id(x) , id(z)
Out[41]: (9788640, 9788640)

In [42]: id(x) is id(z)
Out[42]: False

In [43]: id(x) == id(z)
Out[43]: True

In [44]: x.__repr__
Out[44]: <method-wrapper '__repr__' of int object at 0x955ce0>

In [45]: z.__repr__
Out[45]: <method-wrapper '__repr__' of int object at 0x955ce0>

In [46]: id(2) is id(2)
Out[46]: False

In [47]: id(2) == id(2)
Out[47]: True

In [48]: li1
Out[48]: []

In [49]: li1 is None
Out[49]: False

In [50]: li1 == None
Out[50]: False

In [51]: False is None
Out[51]: False

In [52]: False == None
Out[52]: False
```
|`==`|`is`|
|-|-|
|for value equality|for reference equality|
|Use it when you would like to know if two objects have the same value|Use it when you would like to know if two references refer to the same object.|

> **`id(object)`**
Return the **“identity”** of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

> CPython implementation detail: This is the address of the object in memory.

- *args & **kwargs
```bash
In [54]: def foo(args, kwargs): # correct definiton but NOT desired!
    ...:     print(f'args: {args}')
    ...:     print(f'kwargs: {kwargs}')
    ...: 

In [55]: foo('adnan',29, job='developer')
----------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-55-8f6d72de399a> in <module>
----> 1 foo('adnan',29, job='developer')

TypeError: foo() got an unexpected keyword argument 'job'
###########################################################
# correct definiton
In [56]: def foo(*args, **kwargs):
    ...:     print(f'args: {args}') # args type is tuple
    ...:     print(f'kwargs: {kwargs}') # kwargs type is dict
    ...: 

In [57]: foo('adnan',29, job='developer')
args: ('adnan', 29)
kwargs: {'job': 'developer'}
# ----------------------------------------------------------
In [58]: def foo(*args, **kwargs):
    ...:     print(f'args: {type(args)}')
    ...:     print(f'kwargs: {type(kwargs)}')
    ...: 

In [59]: foo('adnan',29, job='developer')
args: <class 'tuple'>
kwargs: <class 'dict'>
```


#### Resources:
- https://www.toptal.com/python/interview-questions