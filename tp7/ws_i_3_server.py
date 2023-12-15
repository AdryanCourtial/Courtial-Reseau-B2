import asyncio
import random
import datetime
import configparser
import websockets

config_object = configparser.ConfigParser()

config_object.read("config.ini")

userinfo = config_object["SERVERCONFIG"]

ip = userinfo["ipaddr"]
port = userinfo["port"]



async def handle_client_msg(websocket):
    while True:
        try:
            entry = await websocket.read(1024)
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

            addr = websocket.get_extra_info("peername")

            msg = entry.decode()
            print(f"message receive from {addr} : {msg}")

            if not addr in clients:
                    clients[addr] = {}
                    clients[addr]['w'] = websocket
                    if "Hello|" in msg:
                        pseudo = msg[6::]
                        clients[addr]['pseudo'] = pseudo
                        clients[addr]['color'] = random.randint(90,97)
                        for key in clients:
                            w = clients[key]["w"]
                            w.write(f"\n    Annonce : {pseudo} a rejoint la chatroom\n".encode())
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
    async with websockets.serve(handle_client_msg, "10.1.1.11", 13337):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    print(ip, port)
    asyncio.run(main())
