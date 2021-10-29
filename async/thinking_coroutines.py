import asyncio
import datetime
import time
from typing import final


def foo(i):
    print(f"{i} {datetime.datetime.now()}")
    time.sleep(i)


async def async_foo(i):
    """
    This is a co-routine function which creates co-routines
    Desc: instead of creating regular function we create async function for
    not waiting too much!
    """
    now = datetime.datetime.now()
    print(f"{i} {now}")
    await asyncio.sleep(i)
    now = datetime.datetime.now()
    return i, now

# NOTE !!!
# async_foo -> coroutine function
# async_foo(i) -> coroutine
# asyncio.sleep -> coroutine function
# asyncio.sleep(i) -> coroutine
# NOTE How can we invoke coroutines ?
# ANSWER : we just create tasks on loops. Example: loop.create_task(foo(i))


def v1():
    loop = asyncio.get_event_loop()
    # stop event loop after 2 secs
    loop.call_later(2, loop.stop)
    # call foo
    for i in range(1, 4):
        loop.call_soon(foo, i)

    try:
        loop.run_forever()
    finally:
        loop.close()


def v2():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(async_foo(i)) for i in range(1, 4)]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
        print("__________results__________")
        for task in tasks:
            print(*task.result())
            # type(task.result()) : <class 'tuple'>
    finally:
        loop.close()
    """
    1 2021-10-28 22:11:23.688804
    2 2021-10-28 22:11:23.689023
    3 2021-10-28 22:11:23.689143
    __________results__________
    1 2021-10-28 22:11:24.691656
    2 2021-10-28 22:11:25.692053
    3 2021-10-28 22:11:26.691621
    # NOTE Result : some callbacks can take long time but we are able to start them at the same time.
    """


def v3():
    loop = asyncio.get_event_loop()
    task = loop.create_task(async_foo(3))
    try:
        result = loop.run_until_complete(task)
        print("Result: ", *result)
        print("Result: ", *task.result())
    finally:
        loop.close()


def v4():
    loop = asyncio.get_event_loop()
    task = loop.create_task(async_foo('a'))
    try:
        result = loop.run_until_complete(task)
    except TypeError:
        print(f"Type Error: {task.exception()}")
    else:
        print("Result: ", *result)
    finally:
        loop.close()


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
    # v1()
    # v2()
    # v3()
    v4()

"""
PYTHONASYNCIODEBUG=1 python thinking_coroutines.py # helps to see which callback is slow
# NOTE : INVOKING COROUTINES options
1. Outside coroutine options
    a. task = loop.create_task(coro())
    b. result = loop.run_until_complete(coro())
2. Inside coroutine options
    a. task = loop.create_task(coro())
    b. result = await coro()
"""
