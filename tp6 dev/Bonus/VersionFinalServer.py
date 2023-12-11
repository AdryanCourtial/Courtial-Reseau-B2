import asyncio
import random
import datetime

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
                        clients[addr]['color'] = random.randint(90,97)
                        for key in clients:
                            w = clients[key]["w"]
                            w.write(f"\n    Annonce : {pseudo} a rejoint la chatroom".encode())
                            await w.drain()
                            print(f"\nnew client : {addr} with name : {pseudo} so {clients}")
            
            color = clients[addr]['color']

            Timestamp = datetime.datetime.today()
            Timestamp = Timestamp.strftime("%H:%M")
                                
            if "Hello|" not in msg:
                for key in clients:
                    if key == addr:
                        continue
                    else:
                        print(f"sending to {key}")
                        w = clients[key]["w"]
                        w.write(f"[{Timestamp}] \033[{color}m{pseudo}\033[0m a dit :    {msg}".encode())
                        await w.drain()
                        print(f"[{Timestamp} ]\033[{color}m{pseudo}\033[0m a dit :    {msg}")
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

#BONUS