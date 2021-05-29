import asyncio
import datetime


async def server(sec):
    await asyncio.sleep(sec)
    return {"server status": 200}


async def file_reader(sec):
    await asyncio.sleep(sec)
    return {"file": "logfile"}


async def client():
    print(f"client start  : {datetime.datetime.now()}")
    response = await server(3)
    print(response)
    print(f"client end    : {datetime.datetime.now()}")


async def fileio():
    print(f"fileio start  : {datetime.datetime.now()}")
    response = await file_reader(1)
    print(response)
    print(f"fileio end    : {datetime.datetime.now()}")


async def main():
    res_client = asyncio.create_task(client())
    res_fileio = asyncio.create_task(fileio())

    await res_client
    await res_fileio
    

asyncio.run(main())
