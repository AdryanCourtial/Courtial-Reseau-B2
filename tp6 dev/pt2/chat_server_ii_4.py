import asyncio


global clients
client = {}


async def handle_client_msg(reader, writer):
    try:
        entry = await reader.read(1024)
        if entry == b'':
            return None

        addr = writer.get_extra_info("peername")

        msg = entry.decode()
        print(f"message receive from {addr} : {msg}")

        if not addr in client:
                client[addr] = {}
                client[addr]['r'] = reader
                client[addr]['w'] = writer
                print(f"new client : {addr} so {client}")

        for key in client:
            if key == addr:
                print("no not send message to original sender")
                continue
            else:
                print(f"sending to {key}")
                w = client[key]["w"]
                w.write(f"{addr} a dit {msg}".encode())
                await w.drain()
        
        #One Envoie la donné a tout le monde 

    except Exception:
        return Exception

async def main():
    server = await asyncio.start_server(handle_client_msg, "10.1.1.11", port=13337)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())