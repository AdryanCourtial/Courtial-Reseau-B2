import asyncio
import __future__
import aioconsole

ip = "10.1.1.11"
port = 13337  

async def main():
    reader, writer = await asyncio.open_connection(host=ip, port=port)

    writer.write('Hello'.encode())
    await writer.drain()

    while True:
        try:
            tasks = [ async_input(writer), async_receive(reader) ]
            await asyncio.gather(*tasks)

        except Exception: 
            raise Exception
        

async def async_input(writer: asyncio.StreamWriter):
    while True:
        msg = await aioconsole.ainput("Que veux tu écrire ?")
        writer.write((msg.encode()))
        await writer.drain()

async def async_receive(reader: asyncio.StreamReader):
    while True:
        msg = await reader.read(1024)
        if msg == b'':
            break
        print(msg.decode())

if __name__ == "__main__":
    asyncio.run(main())
