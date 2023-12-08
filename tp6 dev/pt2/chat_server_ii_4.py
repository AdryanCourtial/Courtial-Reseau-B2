import asyncio


async def handle_client_msg(reader, writer):
    while True:
        try:
            print("meomeo")
            entry = await reader.read(1024)
            print(entry)

            if entry == b'':
                return None

            addr = writer.get_extra_info("peername")

            msg = entry.decode()
            print(f"message receive from {addr} : {msg}")

            if not addr in clients:
                    clients[addr] = {}
                    clients[addr]['r'] = reader
                    clients[addr]['w'] = writer
                    print(f"new client : {addr} so {clients}")

            for key in clients:
                if key == addr:
                    print("no not send message to original sender")
                    continue
                else:
                    print(f"sending to {key}")
                    w = clients[key]["w"]
                    w.write(f"{addr} a dit {msg}".encode())
                    await w.drain()
            
            print("packet handled")
            #One Envoie la donné a tout le monde 

        except Exception:
            return Exception

async def main():
    
    global clients
    clients = {}
    server = await asyncio.start_server(handle_client_msg, "10.1.1.11", port=13337)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())