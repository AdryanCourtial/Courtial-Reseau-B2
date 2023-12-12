import asyncio
import __future__
import aioconsole
import argparse
import datetime
import logging


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", action="store", default="10.1.1.11")
parser.add_argument("-p", "--port", action="store", default=13337)
args = parser.parse_args()

logging.basicConfig(level=logging.INFO, filename="client.log", filemode="w",
                    format="%(asctimes)s : %(levelname)s : %(message)s")


ip = args.ip
port = args.port  

print(ip, port)

async def main():
    reader, writer = await asyncio.open_connection(host=ip, port=port)

    pseudo = input("Choisi ton nom d'utilisateur : ")
    writer.write(f"Hello|{pseudo}".encode())
    await writer.drain()

    while True:
        try:
            tasks = [ async_input(writer), async_receive(reader) ]
            await asyncio.gather(*tasks)

        except Exception: 
            logging.exception("Exept")
            raise Exception
        

async def async_input(writer: asyncio.StreamWriter):
    while True:
        Timestamp = datetime.datetime.today()
        Timestamp = Timestamp.strftime("%H:%M")
        msg = await aioconsole.ainput("")
        print(f"[{Timestamp}] Vous Avez dit : {msg}")
        logging.INFO(f"[{Timestamp}] Vous Avez dit : {msg}")
        writer.write((msg.encode()))
        await writer.drain()

async def async_receive(reader: asyncio.StreamReader):
    while True:
        msg = await reader.read(1024)
        if msg == b'':
            break
        print(msg.decode())
        logging.INFO(msg.decode())

if __name__ == "__main__":
    asyncio.run(main())
