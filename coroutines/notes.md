# Generators, Coroutines and Nanoservices

```bash

In [1]: def foo():
   ...:     return 1
   ...:     return 2
   ...:     return 3
   ...: 

In [2]: foo()
Out[2]: 1

In [3]: import dis

In [4]: dis.dis(foo)
  2           0 LOAD_CONST               1 (1)
              2 RETURN_VALUE
# line_num	| command 					| value
In [5]: def _gen():
   ...:     yield 1
   ...:     yield 2
   ...:     yield 3
   ...: 

In [6]: _gen()
Out[6]: <generator object _gen at 0x7f2ed71312e0>

In [7]: # yield turns a regular function into a generator function

In [8]: # running a generator function returns a generator object

In [9]: dis.show_code(_gen)
Name:              _gen
Filename:          <ipython-input-5-356b4e8ab381>
Argument count:    0
Positional-only arguments: 0
Kw-only arguments: 0
Number of locals:  0
Stack size:        1
Flags:             OPTIMIZED, NEWLOCALS, GENERATOR, NOFREE # here we see a generator
Constants:
   0: None
   1: 1
   2: 2
   3: 3

In [10]: dis.dis(_gen)
  2           0 LOAD_CONST               1 (1)
              2 YIELD_VALUE
              4 POP_TOP

  3           6 LOAD_CONST               2 (2)
              8 YIELD_VALUE
             10 POP_TOP

  4          12 LOAD_CONST               3 (3)
             14 YIELD_VALUE
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE


```

## What is a Generator?

- It implements Python's iterator protocol
- You get its iterator via `iter` (which is itself)
- You get each succeeded value with `next`
- When it gets to the end it raises `StopIteration`

### How does for loop work ?

```bash
In [11]: for i in 'abcd':
    ...:     print(i)
    ...: 
a
b
c
d
```

- python checks is `'abcd'`is iterable ? If so then repeatedly ask for the next thing, assign to one item and run the loop body.
- When the object raises `StopIteration` exit the loop

### Looping over the generator

```bash
In [5]: def _gen():
   ...:     yield 1
   ...:     yield 2
   ...:     yield 3
In [12]: for i in _gen():
    ...:     print(i)
    ...: 
1
2
3

```

- python checks is `_gen()` is iterable ? (yes it is ) If so then repeatedly ask for the next thing, assign to one item and run the loop body.

```python
In [13]: g = _gen()

In [14]: g
Out[14]: <generator object _gen at 0x7f2ed668a7b0> # address 1

In [15]: iter(g)
Out[15]: <generator object _gen at 0x7f2ed668a7b0> # address 2
# address 1 and address 2 are same.
# so a generator is its own iterator

In [16]: next(g)
Out[16]: 1

In [17]: next(g)
Out[17]: 2

In [18]: next(g)
Out[18]: 3

In [19]: next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-19-e734f8aca5ac> in <module>
----> 1 next(g)

StopIteration:
```

### next and generators

- next tells a generator to run through the next yield statement
- this can be a tiny code or a lot of code
- upon hitting the yield the generator returns the value and goes to sleep
- the function's state remains across those calls

### Example 1

```python
In [20]: def fib():
    ...:     first = 0
    ...:     second = 1
    ...:     while True:
    ...:         yield first
    ...:         first, second = second, first+second
    ...: 

In [21]: f = fib()

In [22]: f
Out[22]: <generator object fib at 0x7f2ed6795c10>

In [23]: next(f)
Out[23]: 0

In [24]: next(f)
Out[24]: 1

In [25]: next(f)
Out[25]: 1

In [26]: next(f)
Out[26]: 2

In [27]: next(f)
Out[27]: 3
##############################
# DONT DO THIS
list(fib()) # the call to list will wait to get StopIteration ...
# which will not ever happen of course
# you will get run out of memory
# NOTE
# This example is a great way to describe an infinitely long sequence
```

### Example 2

```python
In [30]: def _read(filename, n):
    ...:     f = open(filename)
    ...:     while True:
    ...:         out = ''.join(f.readline() for i in range(n))
    ...:         if out:
    ...:             yield out
    ...:         else:
    ...:             break
    ...: 

```

 ### When do we use generators ?

- we have a potentially large or infinite set of values to return
- it's easier to express the idea as a function
- we have to set things up (e.g. a network connection or file)
- we want to keep state across runs in local variables



##### yield as an expression

- The rules for generators still apply
  - Each call to `next` runs the generator through the next `yield`
  - After `yield` it goes to sleep
- But `yield` now allows for two-way communication!
- It can receive a message from the outside world
- The received value replaces `yield` typically assignment

##### the `send` method

- we can advance a generator with the `next` function : `next(g)`

- we can send a value to a generator with the `send` method: `g.send(123)`

- Note : A call to `next(g)` is the same as `g.send(None)`

```python
In [45]: def mycoroutine():
    ..1:     step = 0
    ..2:     while True:
    ..3:         print(f'step:{step}')
    ..4:         received = yield step
    ..5:         print(f'received: {received}')
    ..6:         step +=1
  

In [46]: g = mycoroutine()

In [47]: next(g) # prime or init generator, this step is important, it is like a factory
step:0
Out[47]: 0 # the result of `yield step` expression [line 4]

In [48]: g.send(3) # we send 3 through `received = yield` expression [line 4]. Then program prints, increases step and yield step
received: 3
step:1
Out[48]: 1

In [49]: g.send(10)
received: 10
step:2
Out[49]: 2

```

### This is a coroutine

- A coroutine is a generator
- It waits to get input from elsewhere using `send`
- The data is received with `yield` as an expression(typically on the right side of an assignment)
- Local state remains across calls

### Walrus operator + yield

- Python 3.8 introduced the assignment expression (`:=`)

- ```python
  In [67]: def coro():
      ...:     step = 0
      ...:     while received := (yield step): # if any None or empty value received the loop will be broken
      ...:         print(f'received:{received}')
      ...:         step +=1
      ...: 
  
  In [68]: c = coro()
  
  In [69]: next(c) # for initializing we can use c.send(None)
  Out[69]: 0
  
  In [70]: c.send(100)
  received:100
  Out[70]: 1
  
  In [71]: c.send(44)
  received:44
  Out[71]: 2
  
  In [72]: c.send(None) # break the loop of coroutine
  ---------------------------------------------------------------------------
  StopIteration                             Traceback (most recent call last)
  <ipython-input-72-d9162d5dda48> in <module>
  ----> 1 c.send(None)
  
  StopIteration:
  
  ```





### How can we use coroutines ?

- Database connection example

- ```python
  import psycopg2
  import os
  
  DBNAME = os.environ.get('DB_NAME')
  
  
  class StopUserApiException(Exception):
      pass
  
  
  def userapi():
      conn = psycopg2.connect(f'dbname={DBNAME} user=postgres password=postgres')
      output = 'Send a query or None to quit!'
      while query := (yield output):
          curr = conn.cursor()
          qs = 'SELECT username, is_active FROM auth_user WHERE {}'.format(query)
          print(qs)
  
          curr.execute(qs)
  
          try:
              for single_record in curr.fetchall():
                  yield single_record
          except StopUserApiException:
              continue
  ```

- ```bash
  In [1]: import api_coro
  
  In [2]: api_coro.DBNAME = api_coro.os.environ.get('DBNAME')
  
  In [4]: api = api_coro.userapi()
  
  In [5]: next(api)
  Out[5]: 'Send a query or None to quit!'
  
  In [6]: api.send("email like '%gmail.com%'")
  SELECT username, is_active FROM auth_user WHERE email like '%gmail.com%'
  Out[6]: ('ali.veli', False)
  
  In [7]: api.send("email like '%gmail.com%'") # NOTICE! we are not connecting database again with select query!
  Out[7]: ('fff.ccc', False)
  
  In [8]: api.send("email like '%gmail.com%'")
  Out[8]: ('ddd.vvv', False)
  ############### exit from for loop ###################
  In [9]: api.throw(api_coro.StopUserApiException)
  Out[9]: 'Send a query or None to quit!'
  
  In [10]: api.send("email like '%gmail.com%'") # select query again. because we stopped the 
  SELECT username, is_active FROM auth_user WHERE email like '%gmail.com%'
  Out[10]: ('ali.veli', False)
  ```





- #### yield from

  - used for sub coroutines
  - the way of combining coroutines
  - enables chaining generators and many iterables together



```python


def coro1():
    while d := (yield 'send 1 or None to exit'):
        print(f'coro1 -> d:{d}')


def coro2():
    while d := (yield 'send 2 or None to exit'):
        print(f'coro2 -> d:{d}')


c1 = coro1()
next(c1)
c1.send(100)  # coro1 -> d:100
c1.send(111)  # coro1 -> d:111
print('-'*60)
c2 = coro2()
next(c2)
c2.send(200)  # coro2 -> d:200
c2.send(222)  # coro2 -> d:222


def combined_coro():
    while d := (yield 'SELECT 1 or 2 or None to exit'):
        if d == 1:
            print('selected coro1')
            yield from coro1()
        elif d == 2:
            print('selected coro2')
            yield from coro2()
        else:
            output = 'Unknown choice'


print('_______Combined Coroutine_______')
cc = combined_coro()
next(cc)
cc.send(1)  # we have chosen coro1
cc.send(11)
cc.send(111)
print(cc.send(None)) # we exited from coro1
cc.send(2) # we have chosen coro2
"""
 └─ λ python yield_from.py 
coro1 -> d:100
coro1 -> d:111
------------------------------------------------------------
coro2 -> d:200
coro2 -> d:222
_______Combined Coroutine_______
selected coro1
coro1 -> d:11
coro1 -> d:111
SELECT 1 or 2 or None to exit
selected coro2
"""
```

- ### examples

- ```bash
  In [16]: def internal(name, start, end):
      ...:     for i in range(start, end):
      ...:         value = yield i
      ...:         print(f"{name} got {value}")
      ...:     print(f"{name} finished at {i}")
      ...:     return end
      ...: 
  
  In [17]: def general():
      ...:     start = yield from internal("first", 1,5)
      ...:     end = yield from internal("second", start, 10)
      ...:     return end
      ...: 
  
  In [18]: g = general()
  
  In [19]: next(g)
  Out[19]: 1
  
  In [20]: g.send('1. val sent to main coroutine')
  first got 1. val sent to main coroutine
  Out[20]: 2
  
  In [21]: g.send('another val as 2.')
  first got another val as 2.
  Out[21]: 3
  
  In [22]: g.send('another val as 3.')
  first got another val as 3.
  Out[22]: 4
  
  In [23]: g.send('another val as 4.')
  first got another val as 4.
  first finished at 4
  Out[23]: 5
  
  In [24]: g.send('another val as 5')
  second got another val as 5
  Out[24]: 6
  
  In [25]: g.send('another val as 6')
  second got another val as 6
  Out[25]: 7
  
  In [26]: g.send('another val as 7')
  second got another val as 7
  Out[26]: 8
  
  In [27]: g.send('another val as 8')
  second got another val as 8
  Out[27]: 9
  
  In [28]: g.send('another val as 9')
  second got another val as 9
  second finished at 9
  ---------------------------------------------------------------------------
  StopIteration                             Traceback (most recent call last)
  <ipython-input-28-0c424a1ba8c8> in <module>
  ----> 1 g.send('another val as 9')
  
  StopIteration: 10
  
  ```

- 





