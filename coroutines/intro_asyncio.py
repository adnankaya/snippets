"""
# Async/await
# primarily intended to provide opportunities for the program to execute other code while waiting for a long-running

"""

import asyncio
import datetime
import time


# NOTE example 1
# if __name__ == '__main__':
#     # get event loop for the current thread
#     loop = asyncio.get_event_loop()
#     loop.run_forever()
#     '''
#     # NOTE we are actually running a loop!
#     def run_forever(self):
#         """Run until stop() is called."""
#         # ...
#         try:
#             events._set_running_loop(self)
#             while True:
#                 self._run_once()
#                 if self._stopping:
#                     break
#         finally:
#             self._stopping = False
#             #...
#     '''

# # NOTE example 2


# def foo(i):
#     print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     time.sleep(i)  # NOTE we added this for simulating if any call would be slow


# if __name__ == '__main__':
#     start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"S {start}        ----------process start---------------")
#     loop = asyncio.get_event_loop()
#     loop.call_later(2, loop.stop)  # stop loop after 2 seconds
#     for i in range(1, 5):
#         # as soon as the event loop free, call the foo
#         loop.call_soon(foo, i)
#     try:
#         loop.run_forever()
#     finally:
#         loop.close()
#     end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"E {end}      ----------process end---------------")
# """
#  └─ λ PYTHONASYNCIODEBUG=1 python intro_asyncio.py
# S 2022-01-08 18:36:31        ----------process start---------------
# 1 2022-01-08 18:36:31
# Executing <Handle foo(1) at intro_asyncio.py:29 created at intro_asyncio.py:41> took 1.001 seconds
# 2 2022-01-08 18:36:32
# Executing <Handle foo(2) at intro_asyncio.py:29 created at intro_asyncio.py:41> took 2.001 seconds
# 3 2022-01-08 18:36:34
# Executing <Handle foo(3) at intro_asyncio.py:29 created at intro_asyncio.py:41> took 3.003 seconds
# 4 2022-01-08 18:36:37
# Executing <Handle foo(4) at intro_asyncio.py:29 created at intro_asyncio.py:41> took 4.004 seconds
# E 2022-01-08 18:36:41      ----------process end---------------

# # NOTE our regular foo function is getting slower, how can we solve this problem ?
# # TODO see example 3
# """


# # NOTE example 3 : creating coroutine function

# async def foo(i):
#     '''this is a coroutine function, when we call it foo(i) then this is a coroutine'''
#     print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     await asyncio.sleep(i)  # this is a coroutine too!

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.call_later(2, loop.stop)
#     # to call a coroutine we create task
#     for i in range(1, 5):
#         # just execute this asyncronously
#         loop.create_task(foo(i))
#     try:
#         loop.run_forever()
#     finally:
#         loop.close()
#     """
#      └─ λ PYTHONASYNCIODEBUG=1 python intro_asyncio.py
# 1 2022-01-08 20:13:34
# 2 2022-01-08 20:13:34
# 3 2022-01-08 20:13:34
# 4 2022-01-08 20:13:34
# Task was destroyed but it is pending!
# source_traceback: Object created at (most recent call last):
#   File "intro_asyncio.py", line 79, in <module>
#     loop.create_task(foo(i))
# task: <Task pending name='Task-2' coro=<foo() running at intro_asyncio.py:71> wait_for=<Future finished result=None created at /usr/lib/python3.8/asyncio/base_events.py:422> created at intro_asyncio.py:79>
# Task was destroyed but it is pending!
# source_traceback: Object created at (most recent call last):
#   File "intro_asyncio.py", line 79, in <module>
#     loop.create_task(foo(i))
# task: <Task pending name='Task-3' coro=<foo() done, defined at intro_asyncio.py:68> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7f1f388a2700>()] created at /usr/lib/python3.8/asyncio/base_events.py:422> created at intro_asyncio.py:79>
# Task was destroyed but it is pending!
# source_traceback: Object created at (most recent call last):
#   File "intro_asyncio.py", line 79, in <module>
#     loop.create_task(foo(i))
# task: <Task pending name='Task-4' coro=<foo() done, defined at intro_asyncio.py:68> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7f1f388a22e0>()] created at /usr/lib/python3.8/asyncio/base_events.py:422> created at intro_asyncio.py:79>

#     """

# # NOTE example 4 :

# async def foo(i):
#     '''this is a coroutine function, when we call it foo(i) then this is a coroutine'''
#     print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     await asyncio.sleep(i)  # this is a coroutine too!

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     # to call a coroutine we create task
#     tasks = [loop.create_task(foo(i)) for i in range(1, 5)]
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))  # wait on tasks
#     finally:
#         loop.close()
#     """
#      └─ λ PYTHONASYNCIODEBUG=1 python intro_asyncio.py 
# 1 2022-01-08 21:43:05
# 2 2022-01-08 21:43:05
# 3 2022-01-08 21:43:05
# 4 2022-01-08 21:43:05
# """

# # NOTE example 5 :

# async def foo(i):
#     '''this is a coroutine function, when we call it foo(i) then this is a coroutine'''
#     print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     await asyncio.sleep(i)  # this is a coroutine too!
#     return i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     # to call a coroutine we create task
#     tasks = [loop.create_task(foo(i)) for i in range(1, 5)]
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))  # wait on tasks
#         for task in tasks:
#             print(*task.result())
#     finally:
#         loop.close()
#     """
#  └─ λ PYTHONASYNCIODEBUG=1 python intro_asyncio.py 
# 1 2022-01-08 21:46:44 # NOTE executing concurrently the tasks, we are able to start them sort of at the same time
# 2 2022-01-08 21:46:44 # NOTE executing concurrently the tasks, we are able to start them sort of at the same time
# 3 2022-01-08 21:46:44 # NOTE executing concurrently the tasks, we are able to start them sort of at the same time
# 4 2022-01-08 21:46:44 # NOTE executing concurrently the tasks, we are able to start them sort of at the same time
# 1 2022-01-08 21:46:45 # NOTE results
# 2 2022-01-08 21:46:46 # NOTE results
# 3 2022-01-08 21:46:47 # NOTE results
# 4 2022-01-08 21:46:48 # NOTE results
# # NOTE we are executing the tasks first and then gathering the results

# # NOTE if we had only one task
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(foo(3))
#     try:
#         result = loop.run_until_complete(task)
#         print(*result)
#     finally:
#         loop.close()
# """

# # NOTE example 6 : exception handling

# async def foo(i):
#     '''this is a coroutine function, when we call it foo(i) then this is a coroutine'''
#     print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     await asyncio.sleep(i)  # this is a coroutine too!
#     return i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(foo('g'))
#     try:
#         result = loop.run_until_complete(task)
#     except TypeError:
#         print('Type error: ', task.exception())
#     else:
#         print(*result)
#     finally:
#         loop.close()
# """
#  └─ λ PYTHONASYNCIODEBUG=1 python intro_asyncio.py 
# g 2022-01-08 21:55:58
# Type error:  '<=' not supported between instances of 'str' and 'int'

# # NOTE instead of getting this error in the main scope we can handle it in the coroutine
# async def foo(i):
#     print(i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     try:
#         await asyncio.sleep(i)
#     except TypeError:
#         i = 0
#     return i, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
# """

# """
# # NOTE invoking coroutines
# # outside a coroutine
# task = loop.create_task(coro()) # NOTE
# result = loop.run_until_complete(coro())
# # inside a coroutine
# task = loop.create_task(coro()) # NOTE
# result = await coro()

# """

# NOTE example 7 : setup for debugging

if __name__ == '__main__':
    """NOTE: for debugging
    import logging
    log = logging.getLogger('asyncio')
    log.setLevel(logging.DEBUG)
    import gc
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    try:
        loop.run_forever()
    finally:
        loop.close()
    """
    