import asyncio


async def fetch_data():
    await asyncio.sleep(3)
    return {"data": 100}


async def count_down():
    for i in range(10, 0, -1):
        await asyncio.sleep(.5)
        print(i)
        


async def main():
    res_fd = asyncio.create_task(fetch_data())
    res_cd = asyncio.create_task(count_down())

    await res_fd
    print(res_fd.result())
    await res_cd



asyncio.run(main())
