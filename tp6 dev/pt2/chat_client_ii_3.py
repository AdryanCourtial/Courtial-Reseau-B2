import socket
import asyncio
import __future__

ip = "10.1.1.11"
port = 13337

async def main():
    reader, writer = await asyncio.open_connection(host=ip, port=port)

    writer.write('Hello'.encode())
    await writer.drain()

    entry = await reader.read(1024)
    print(entry.decode())

if __name__ == "__main__":
    asyncio.run(main())