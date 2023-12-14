import asyncio
import websockets

async def hello():
    uri = "ws://10.1.1.11:13337"
    async with websockets.connect(uri) as websocket:
        name = input("")

        await websocket.send(name)

        data = await websocket.recv()
        print(f"{data}")

if __name__ == "__main__":
    asyncio.run(hello())
