import asyncio


global clients
client = {}


async def handle_client_msg(reader, writer):
    while True:
        try:
            entry = await reader.read(1024)
            if entry == b'':
                break

            addr = writer.get_extra_info("peername")
            client[addr] = {}

            msg = entry.decode()
            print(f"message receive from {addr} : {msg}")

            if client[addr] == {}:
                    client[addr]['r'] = reader
                    client[addr]['w'] = writer

            for key in client.keys():
                if key == addr:
                    continue
                else:
                    client[addr]['r'] = reader
                    client[addr]['w'] = writer #FAUT FAIRE DE LASYNCRINE QUELQUE PARTY

            print(client)                    
            
            #One Envoie la donné a tout le monde 

            for key in client.keys():
                if key == addr:
                    continue
                else:
                    client[key].write(f"{addr} a dit {msg}".encode())
                    await writer.drain()

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