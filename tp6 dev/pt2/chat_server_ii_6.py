import asyncio

async def handle_client_msg(reader, writer):
    while True:
        try:
            entry = await reader.read(1024)
            print(entry)

            if entry == b'':
                for key in clients:
                    print(f"deco de {pseudo}")
                    w = clients[key]["w"]
                    w.write(f"\n            {pseudo} C DECONNECTER \n".encode())
                    await w.drain()
                    del clients[addr]
                    print(clients)
                return None

            addr = writer.get_extra_info("peername")

            msg = entry.decode()
            print(f"message receive from {addr} : {msg}")

            if not addr in clients:
                    clients[addr] = {}
                    clients[addr]['r'] = reader
                    clients[addr]['w'] = writer
                    if "Hello|" in msg:
                        pseudo = msg[6::]
                        clients[addr]['pseudo'] = pseudo
                        for key in clients:
                            w = clients[key]["w"]
                            w.write(f"\n    Annonce : {pseudo} a rejoint la chatroom".encode())
                            await w.drain()
                            print(f"\nnew client : {addr} with name : {pseudo} so {clients}")
                                
            if "Hello|" not in msg:
                for key in clients:
                    if key == addr:
                        continue
                    else:
                        print(f"sending to {key}")
                        w = clients[key]["w"]
                        w.write(f"{pseudo} a dit :    {msg}".encode())
                        await w.drain()
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

    #TPFINI (YA 5ET6)