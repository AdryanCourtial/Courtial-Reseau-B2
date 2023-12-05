import asyncio

async def count1():
    for x in range (11):
        print(x)
        await asyncio.sleep(0.5) 

loop = asyncio.get_event_loop()


tasks = [
    loop.create_task(count1()),
    loop.create_task(count1()),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

