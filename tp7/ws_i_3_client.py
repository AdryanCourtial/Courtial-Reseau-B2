import asyncio
import __future__
import aioconsole
import argparse
import datetime
import websockets

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", action="store", default="10.1.1.11")
parser.add_argument("-p", "--port", action="store", default=13337)
args = parser.parse_args()


ip = args.ip
port = args.port  

print(ip, port)

async def main():
    uri = "10.1.1.11:13337"
    async with websockets.connect(uri) as websocket:

        pseudo = input("Choisi ton nom d'utilisateur : ")
        await websocket.send(f"Hello|{pseudo}")

        while True:
            try:
                tasks = [ async_input(websocket), async_receive(websocket) ]
                await asyncio.gather(*tasks)

            except Exception: 
                raise Exception
        

async def async_input(websocket:websockets):
    while True:
        Timestamp = datetime.datetime.today()
        Timestamp = Timestamp.strftime("%H:%M")
        msg = await aioconsole.ainput("")
        print(f"[{Timestamp}] Vous Avez dit :   {msg}")
        await websocket.send(msg)

async def async_receive(websocket:websockets):
    while True:
        msg = await websocket.recv()
        if msg == b'':
            break
        print(msg)

if __name__ == "__main__":
    asyncio.run(main())