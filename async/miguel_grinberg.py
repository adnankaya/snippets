import asyncio
from asyncio import tasks
import datetime
import time


def timer(func):
    def f(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"Elapsed duration: {after-before}")

    return f


def hello(i):
    print(f'{i} Hello!')
    time.sleep(1)
    print(f'{i} World!')


@timer
def hello_main():
    for i in range(10):
        hello(i)


loop = asyncio.get_event_loop()


async def hello_async(i):
    print(f'{i} Hello!')
    await asyncio.sleep(1)
    print(f'{i} World!')


async def hello_async_main():
    tasks = []
    for i in range(10):
        task = loop.create_task(hello_async(i))
        tasks.append(task)
    return await asyncio.gather(*tasks)


@timer
def measure():
    loop.run_until_complete(hello_async_main())


if __name__ == '__main__':
    print("-----Sync-----")
    hello_main()
    print("-----A-Sync-----")
    measure()
