# Python interview Questions and Answers
1. What is the difference between a list and a tuple?

|Lists|Tuples|
|-|-|
|Mutable|Immutable|
|Slower|Faster|
|Ordered|Ordered|
|Can have different types|Can have different types|
|over-allocate|not over allocate, so fixed sized|

2. How is string interpolation performed?
Without Template class there are 3 ways to interpolate
```bash
>>> name = 'adnan'
>>> # 1. f strings
>>> f'my name is {name}'
'my name is adnan'
>>> # 2. % operator
>>> 'Hello %s %s %s' % (name, name, name)
'Hello adnan adnan adnan'
>>> # 3. format
>>> '{}! where are you?'.format(name)
'adnan! where are you?'
>>> '{param}! where are you? {second_param}'.format(param=name, second_param=name)
'adnan! where are you? adnan'
```
3. What is the difference between “is” and “==”?
`is` checks identity and `==` checks equality.
```bash
>>> a = [2, "a", 3.14]
>>> b = a
>>> c = [2, "a", 3.14]
>>> # checking with '=='
>>> a == b
True
>>> a == c
True
>>> # checking with 'is'
>>> a is b
True
>>> a is c
False
>>> # Verify by printing object id's
>>> print( id(a) )
140246413499904 # same with b
>>> print( id(b) )
140246413499904 # same with a
>>> print( id(c) )
140246412145984 # different from a and b
```
4. What is a decorator ?
- A decorator allows adding functionality to an existing function. 
- By passing that existing function to a decorator, which executes the exsiting function as well as additional code. 
```python
In [1]: def logger(func):
   ...:     def wrapper():
   ...:         print(f'{func.__name__} called.')
   ...:         func()
   ...:     return wrapper
   ...: 

In [2]: @logger
   ...: def foo():
   ...:     print('inside foo!')
   ...: 

In [3]: foo()
foo called.
inside foo!
```

5. Explain the range function
Range generates a list of integers and there are 3 ways to use it
```python
In [1]: m_range = range(10) # from 0 to 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
In [2]: len(m_range)
Out[2]: 10

In [3]: type(m_range)
Out[3]: range

In [4]: [i**2 for i in m_range]
Out[4]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

In [5]: [i*10 for i in range(2,7)] # from 2 to 7
Out[5]: [20, 30, 40, 50, 60]

In [6]: [i/2 for i in range(2,17,3)] # from 2 to 17 and step is 3
Out[6]: [1.0, 2.5, 4.0, 5.5, 7.0]
In [7]: [i for i in range(2,17,3)]
Out[7]: [2, 5, 8, 11, 14]
```
6. Define a class named car with 2 attributes, “color” and “speed”. Then create an instance and return speed.
```bash
In [1]: class Car:
   ...:     def __init__(self, name, speed):
   ...:         self.name = name
   ...:         self.speed = speed
   ...: 

In [2]: car = Car('BMW', 320)

In [3]: car.speed
Out[3]: 320

```
7. What is the difference between instance, static and class methods in python?
- **Instance methods** : accept self parameter and relate to a specific instance of the class.
- **Static methods** : use @staticmethod decorator, are not related to a specific instance, and are self-contained (don’t modify class or instance attributes)
- **Class methods** : accept cls parameter and can modify the class itself

```bash
In [1]: class CoffeeShop:
    ...:     specialty = 'espresso'
    ...: 
    ...:     def __init__(self, coffee_price):
    ...:         self.coffee_price = coffee_price
    ...: 
    ...:     # instance method
    ...:     def make_coffee(self):
    ...:         print(f'Making {self.specialty} for ${self.coffee_price}')
    ...: 
    ...:     # static method    
    ...:     @staticmethod
    ...:     def check_weather():
    ...:         print('Its sunny')
    ...:     # class method
    ...:     @classmethod
    ...:     def change_specialty(cls, specialty):
    ...:         cls.specialty = specialty
    ...:         print(f'Specialty changed to {specialty}')
    ...: 

In [2]: cs = CoffeeShop(15)

In [3]: cs.make_coffee()
Making espresso for $15

In [4]: cs.check_weather()
Its sunny

In [5]: cs.change_specialty('Turkish Coffee')
Specialty changed to Turkish Coffee

In [6]: cs.make_coffee()
Making Turkish Coffee for $15

In [7]: cs.specialty
Out[7]: 'Turkish Coffee'

In [8]: cs.specialty = 'Arabian Coffee'

In [9]: cs.make_coffee()
Making Arabian Coffee for $15

# Change speciality of class variable
In [10]: CoffeeShop.change_specialty('African Coffe')
Specialty changed to African Coffe

In [11]: cs.make_coffee()
Making Arabian Coffee for $15 # Attention! instance cs keeps its speciality!!!

# new instances will have new speciality which has been changed as African Coffe
In [12]: cs2 = CoffeeShop(33)

In [13]: cs2.make_coffee()
Making African Coffe for $33
```
8. What is the difference between “func” and “func()”?
```bash
In [1]: def func():
    ...:     print("I'm a function")
    ...: 

In [2]: func # object representation
Out[2]: <function __main__.func()>

In [3]: func() # we call func by using ()
I'm a function
```
9. Explain how the map function works
- `map` returns a map object (an iterator) which can iterate over returned values from applying a function to every element in a sequence. The map object can also be converted to a list if required.
```bash
In [1]: li = [2, 5, 1]

In [2]: def square(var):
    ...:     return var**2
    ...: 

In [3]: map(square, li)
Out[3]: <map at 0x7efe05d5a7f0>

In [4]: [i for i in map(square, li)]
Out[4]: [4, 25, 1]

In [5]: list(map(square, li))
Out[5]: [4, 25, 1]
```
10. Explain how the reduce function works
- `reduce` takes a "function" and "a sequence" and iterates over that sequence. 
- On each iteration, both the current element and output from the previous element are passed to the function. 
- In the end, a single value is returned.
- **reduce takes a function which have only 2 parameters** but you can customize
```bash
In [1]: from functools import reduce

In [2]: def add(s1, s2):
    ...:     return s1+s2
    ...: 

In [3]: li = [2, 5, 1, 10]

In [4]: reduce(add, li)
Out[4]: 18

In [5]: def foo(v1, v2, v3):
    ...:     return v1*v2*v3
    ...: 

In [6]: reduce(foo, li)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-a4852a3a1cab> in <module>
----> 1 reduce(foo, li)

TypeError: foo() missing 1 required positional argument: 'v3'
```

11. Explain how the filter function works
- Filter literally does what the name says. It filters elements in a sequence.
- Each element is passed to a function which is returned in the outputted sequence if the function returns True and discarded if the function returns False.
```bash
In [1]: def check(x):
    ...:     if x%2 == 0:
    ...:         return True
    ...:     return False
    ...: 

In [2]: li = [2, 5, 1, 10]

In [3]: filter(check, li)
Out[3]: <filter at 0x7efe053a79d0>

In [4]: list(filter(check, li))
Out[4]: [2, 10]

In [5]: [i for i in filter(check, li)]
Out[5]: [2, 10]

```
12. Does python call by reference or call by value?
- In a nutshell, **all names call by reference**, but some memory locations hold objects while others hold pointers to yet other memory locations.
```bash
In [1]: x = 'adnan'

In [2]: y = x

In [3]: x is y
Out[3]: True

In [4]: del x

In [5]: x
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-52-6fcf9dfbd479> in <module>
----> 1 x

NameError: name 'x' is not defined

In [6]: z = y

In [7]: y is z
Out[7]: True
```
```python
name = 'text'
def add_chars(str1):
    print( id(str1) ) #=> 4353702856
    print( id(name) ) #=> 4353702856
    
    # new name, same object
    str2 = str1
    
    # creates a new name (with same name as the first) AND object
    str1 += 's' 
    print( id(str1) ) #=> 4387143328
    
    # still the original object
    print( id(str2) ) #=> 4353702856
    
    
add_chars(name)
print(name) #=>text
```
13. How to reverse a list?
```bash
In [1]: li
Out[1]: [2, 5, 1, 10]

In [2]: li.reverse() # it does not return a list!!! it returns None!!

In [3]: li
Out[3]: [10, 1, 5, 2]
In [4]: id(li)
Out[4]: 139629246714112

In [5]: x = li.reverse()

In [6]: id(x)
Out[6]: 9484816

In [7]: x

In [8]: type(x)
Out[8]: NoneType

```
14. How does string multiplication work?
```bash
In [1]: 'a' * 5
Out[1]: 'aaaaa'
```
15. How does list multiplication work?
```bash
In [1]: li
Out[1]: [2, 5, 1, 10]

In [2]: li * 2
Out[2]: [2, 5, 1, 10, 2, 5, 1, 10]

In [3]: li1 = [2,3]

In [4]: li2 = [5, 10]

In [5]: li1 * li2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-70-595ba784bf5e> in <module>
----> 1 li1 * li2

TypeError: can't multiply sequence by non-int of type 'list'
```
16. What does “self” refer to in a class?
- **self** refers to the instance of the class itself. 
- It’s how we give methods access to and the ability to update the object they belong to.
Below, passing self to `__init__()` gives us the ability to set the color of an instance on initialization.
```python
class Shirt:
    def __init__(self, color):
        self.color = color
        
s = Shirt('yellow')
s.color
#=> 'yellow'
```
17. How can you concatenate lists in python?
```bash
In [1]: li1 = ['a',29]

In [2]: li2 = ['k', 3]

In [3]: li1 + li2
Out[3]: ['a', 29, 'k', 3]

In [4]: li1.extend(li2)

In [5]: li1
Out[5]: ['a', 29, 'k', 3]

In [6]: li2
Out[6]: ['k', 3]

In [7]: li3 = ['z', 22]

In [8]: [*li2, *li3]
Out[8]: ['k', 3, 'z', 22]
```
18. What is the difference between a shallow and a deep copy?
```bash
In [1]: li2
Out[1]: ['k', 3]

In [2]: li3
Out[2]: ['z', 22]

In [3]: li4 = li2 # li2 and li4 points to same object and have same reference

In [4]: li2.append('i')

In [5]: li2
Out[5]: ['k', 3, 'i']

In [6]: li4
Out[6]: ['k', 3, 'i']
```
- **Create a shallow copy of the original**:
   - We can do this with the list() constructor, 
   - or the more pythonic mylist.copy()
- A shallow copy creates a new object, but fills it with references to the original. 
- So adding a new object to the original collection, `orig`, doesn’t propagate to `copied`, but modifying one of the objects in `orig` will propagate to `copied`.
```bash
In [1]: orig = [['a'],['b'],['c']]

In [2]: copied = list(orig)

In [3]: id(copied) == id(orig)
Out[3]: False

In [4]: orig.append([4])

In [5]: copied
Out[5]: [['a'], ['b'], ['c']]

In [6]: orig
Out[6]: [['a'], ['b'], ['c'], [4]]

In [7]: orig[1][0] = ['x']

In [8]: copied
Out[8]: [['a'], [['x']], ['c']]

In [9]: orig
Out[9]: [['a'], [['x']], ['c'], [4]]
```
- **Create a deep copy**. This is done with copy.deepcopy(). The 2 objects are now completely independent and changes to either have no affect on the other.
```bash
In [1]: import copy

In [2]: orig = [['a'],['b'],['c']]

In [3]: copied = copy.deepcopy(orig)

In [4]: orig.append([4])

In [5]: orig
Out[5]: [['a'], ['b'], ['c'], [4]]

In [6]: copied
Out[6]: [['a'], ['b'], ['c']]

In [7]: orig[1][0] = [23]

In [8]: orig
Out[8]: [['a'], [[23]], ['c'], [4]]

In [9]: copied
Out[9]: [['a'], ['b'], ['c']]
```
19. What is the difference between lists and arrays?
> Note: Python’s standard library has an array object but here I’m specifically referring to the commonly used Numpy array.
- Lists exist in python’s standard library. Arrays are defined by Numpy.
- Lists can be populated with different types of data at each index. Arrays require homogeneous elements.
- Arithmetic on lists adds or removes elements from the list. Arithmetic on arrays functions per linear algebra.
- Arrays also use less memory and come with significantly more functionality.

20. How to concatenate two arrays?
- Remember, arrays are not lists. Arrays are from Numpy and arithmetic functions like linear algebra
```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
np.concatenate((a,b))
#=> array([1, 2, 3, 4, 5, 6])
```
21. Name mutable and immutable objects in Python

|Type	|Immutable?|
|-|-|
|int|	Yes|
|float|	Yes|
|bool|	Yes|
|complex|	Yes|
|tuple|	Yes|
|frozenset|	Yes|
|str|	Yes|
|**list**|	No|
|**set**|	No|
|**dict**|	No|

22. How would you round a number to 3 decimal places?
- Use the round(value, decimal_places) function.
```bash
In [1]: x = 3.14159

In [2]: round(x)
Out[2]: 3

In [3]: round(x, 2)
Out[3]: 3.14

In [4]: round(x, 4)
Out[4]: 3.1416
```
23. How do you slice a list?
- Slicing notation takes 3 arguments, `list[start:stop:step]`, where step is the interval at which elements are returned.
```bash
In [1]: a = [0,1,2,3,4,5,6,7,8,9]

In [2]: a[:2]
Out[2]: [0, 1]

In [3]: a[3:6]
Out[3]: [3, 4, 5]

In [4]: a[::2]
Out[4]: [0, 2, 4, 6, 8]

In [5]: a[::-1] # reversing is easy :D
Out[5]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
24. What is pickling?
- Pickling is the go-to method of serializing and unserializing objects in Python.
```bash
In [1]: import pickle

In [2]: dict_list = [
   ...: {'id':1, 'name':'Adnan'},
   ...: {'id':2, 'name':'Kaya'}
   ...: ]

In [3]: with open('pickle_file.p', 'wb') as f: pickle.dump(dict_list, f)

In [4]: with open('pickle_file.p', 'rb') as f:
   ...:     loaded = pickle.load(f)
   ...: 

In [5]: print(loaded)
[{'id': 1, 'name': 'Adnan'}, {'id': 2, 'name': 'Kaya'}]  
```
25. What is the difference between dictionaries and JSON?
- Dict is python datatype, a collection of indexed but unordered keys and values.
- JSON is just a string which follows a specified format and is intended for transferring data.

26. How do `any()` and `all()` work?
- `any()` takes a sequence and returns true if any element in the sequence is true.
- `all()` takes a sequence returns true only if all elements in the sequence are true.
```bash
In [6]: a = [False, False, False]
   ...: b = [True, False, False]
   ...: c = [True, True, True]
   ...: 

In [7]: print(any(a),'\t', any(b), '\t', any(c))
False    True    True

In [8]: print(all(a),'\t', all(b), '\t', all(c))
False    False   True
```
27. Are dictionaries or lists faster for lookups?
- Looking up a value in a list takes `O(n)` time because the whole list needs to be iterated through until the value is found.
- Looking up a key in a dictionary takes `O(1)` time because it’s a hash table.

- This can make a huge time difference if there are a lot of values so dictionaries are generally recommended for speed
- But they do have other limitations like needing unique keys.

28. What is the difference between a module and a package?
- A module is a file (or collection of files) that can be imported together.
`import sklearn`
- A package is a directory of modules.
`from sklearn import cross_validation`
> So packages are modules, but not all modules are packages.

29. How to increment and decrement an integer in Python?
- Increments and decrements can be done with `+=` and `-=` .
```python
value = 5
value += 1
print(value)
#=> 6
value -= 1
value -= 1
print(value)
#=> 4
```
30. How to return the binary of an integer?
```bash
In [1]: bin(23)
Out[1]: '0b10111'
```
31. How to remove duplicate elements from a list?
```bash
In [1]: li = [2, 3, 2, 3, 4, 5, 1, 0, 0, 0]

In [2]: set(li) # A set is an unordered collection with no duplicate elements
Out[2]: {0, 1, 2, 3, 4, 5}

In [3]: list(set(li))
Out[3]: [0, 1, 2, 3, 4, 5]
```
32. How to check if a value exists in a list?
```bash
In [1]: x
Out[1]: [1, 2, 3, 4, 66, 6, 9, 12]

In [2]: 44 in x
Out[2]: False

In [3]: 66 in x
Out[3]: True
```
33. What is the difference between `append` and `extend`?
- `append` adds a value to a list while `extend` adds values in another list to a list.
```python
a = [1,2,3]
b = [1,2,3]
a.append(6)
print(a)
#=> [1, 2, 3, 6]
b.extend([4,5])
print(b)
#=> [1, 2, 3, 4, 5]
```
34. How to take the absolute value of an integer?
This can be done with the abs() function.
```python
abs(2)
#=> 2
abs(-2)
#=> 2
```
35. How to combine two lists into a list of tuples?
```bash
In [25]: li1 = [2, 9, 1]

In [26]: li2 = [3, 99, 0]

In [27]: zip(li1, li2)
Out[27]: <zip at 0x7f6696dc4500>

In [28]: [k,v for k,v in zip(li1, li2)]
  File "<ipython-input-28-d68036aef6b0>", line 1
    [k,v for k,v in zip(li1, li2)]
         ^
SyntaxError: invalid syntax


In [29]: [(k,v) for k,v in zip(li1, li2)]
Out[29]: [(2, 3), (9, 99), (1, 0)]
```
36. How can you sort a dictionary by key, alphabetically?
- You can’t “sort” a dictionary because dictionaries don’t have order but you can return a sorted list of tuples which has the keys and values that are in the dictionary.
```bash
In [1]: d = {'e':23, 'a':44, 'c':1, 'b':5, 'd':55}

In [2]: d
Out[2]: {'e': 23, 'a': 44, 'c': 1, 'b': 5, 'd': 55}

In [3]: d.items()
Out[3]: dict_items([('e', 23), ('a', 44), ('c', 1), ('b', 5), ('d', 55)])

In [4]: type(d.items())
Out[4]: dict_items

In [5]: sorted(d.items())
Out[5]: [('a', 44), ('b', 5), ('c', 1), ('d', 55), ('e', 23)]
```
37. How does a class inherit from another class in Python?
```python
class Car():
    def drive(self):
        print('vroom')
class Audi(Car):
    pass
audi = Audi()
audi.drive()
```
38. How can you remove all whitespace from a string?
- The easiest way is to split the string on whitespace and then rejoin without spaces.
```python
s = 'A string with     white space'
''.join(s.split())
#=> 'Astringwithwhitespace'
```
- `replace` is faster because python doesn’t create a new list object.
```python
s = 'A string with     white space'
s.replace(' ', '')
#=> 'Astringwithwhitespace'
```
39. Why would you use `enumerate()` when iterating on a sequence?
- `enumerate()` allows tracking index when iterating over a sequence. It’s more pythonic than defining and incrementing an integer representing the index.
```python
li = ['a','b','c','d','e']
for idx,val in enumerate(li):
    print(idx, val)
#=> 0 a
#=> 1 b
#=> 2 c
#=> 3 d
#=> 4 e
```
40. What is the difference between pass, continue and break?
- `pass` means do nothing. We typically use it because Python doesn’t allow creating a class, function or if-statement without code inside it.
```bash
a = [1,2,3,4,5]
for i in a:
    if i > 3:
        pass
    print(i)
#=> 1
#=> 2
#=> 3
#=> 4
#=> 5
```
- `continue` continues to the next element and halts execution for the current element. So print(i) is never reached for values where i < 3.
```python
a = [1,2,3,4,5]
for i in a:
    if i < 3:
        continue
    print(i)
#=> 3
#=> 4
#=> 5
```
- `break` breaks the loop and the sequence is not longer iterated over. So elements from 3 onward are not printed.
```python
a = [1,2,3,4,5]
for i in a:
    if i == 3:
        break
    print(i)    
#=> 1
#=> 2
```
41. Convert the following for loop into a list comprehension.
```python
a = [1,2,3,4,5]
 
a2 = []
for i in a:
     a2.append(i + 1)
print(a2)
#=> [2, 3, 4, 5, 6]
# comprehension
[i+1 for i in a]
#=> [2, 3, 4, 5, 6]
```
41. Give an example of the ternary operator.
- The ternary operator is a one-line if/else statement.
- The syntax looks like `a if condition else b`.
```bash
In [1]: x, y = 5, 7

In [2]: x, y
Out[2]: (5, 7)

In [3]: "gt 4" if x > 4 else "lt 4"
Out[3]: 'gt 4'
```
42. Check if a string only contains numbers.
- You can use `isnumeric()`.
```bash
In [1]: "123".isnumeric()
Out[1]: True

In [2]: "123x".isnumeric()
Out[2]: False
```
43. Check if a string only contains letters.
You can use isalpha().
```python
'123a'.isalpha()
#=> False
'a'.isalpha()
#=> True
```
44. Check if a string only contains numbers and letters.
You can use isalnum()
```python
'123abc...'.isalnum()
#=> False
'123abc'.isalnum()
#=> True
```
45. Return a list of keys from a dictionary.
- This can be done by passing the dictionary to python’s list() constructor, list().
```bash
In [1]: d = {'a':23, 'b':44, 'c':55}

In [2]: d.keys()
Out[2]: dict_keys(['a', 'b', 'c'])

In [3]: list(d)
Out[3]: ['a', 'b', 'c']
```
46. How do you upper and lowercase a string?
- You can use the upper() and lower() string methods.
```python
small_word = 'potatocake'
big_word = 'FISHCAKE'
small_word.upper()
#=> 'POTATOCAKE'
big_word.lower()
#=> 'fishcake'
```
47. What is the difference between `remove`, `del` and `pop`?
- `remove()` remove the first matching value.
- `del` removes an element by index.
- `pop()` removes an element by index and returns that element.
```bash
In [54]: li = ['a','b','c','d','c']

In [55]: li.remove('c')

In [56]: li
Out[56]: ['a', 'b', 'd', 'c']

In [57]: del li[0]

In [58]: li
Out[58]: ['b', 'd', 'c']

In [59]: li.pop(2)
Out[59]: 'c'

In [60]: li
Out[60]: ['b', 'd']

In [61]: li.pop() # removes last element if index is not given
Out[61]: 'd'

In [62]: li
Out[62]: ['b']
```
48. Give an example of dictionary comprehension.
```bash
In [1]: import string

In [2]: alphabet = list(string.ascii_lowercase)

In [3]: d = { letter:index for index, letter in enumerate(alphabet,start=1)}

In [4]: d
print(d)
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
```
49. How is exception handling performed in Python?
- Python provides 3 words to handle exceptions, try, except and finally.
The syntax looks like this.
```bash
try:
    # try to do this
except:
    # if try block fails then do this
finally:
    # always do this
```
```bash
try:
    val = 1 + 'A'
except:
    val = 10
finally:
    print('complete')
    
print(val)
#=> complete
#=> 10
###################################################
In [70]: try:
    ...:     val = 1 + 'A'
    ...: except Exception as e:
    ...:     raise e
    ...: finally:
    ...:     print('*** finally block ***')
    ...: 
    ...: print(val)
# output 
*** finally block ***
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-70-0110bd7a0ae6> in <module>
      2     val = 1 + 'A'
      3 except Exception as e:
----> 4     raise e
      5 finally:
      6     print('*** finally block ***')

<ipython-input-70-0110bd7a0ae6> in <module>
      1 try:
----> 2     val = 1 + 'A'
      3 except Exception as e:
      4     raise e
      5 finally:

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```



### Source
- https://towardsdatascience.com/53-python-interview-questions-and-answers-91fa311eec3f