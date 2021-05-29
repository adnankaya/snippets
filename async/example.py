import asyncio


async def t1():
    await t2()
    print(t1.__name__)


async def t2():
    print(t2.__name__)


async def t3():
    await t1()
    print(t3.__name__)

asyncio.run(t3())
