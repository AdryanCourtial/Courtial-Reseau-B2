import socket
import asyncio
import __future__
import aioconsole

ip = "10.1.1.11"
port = 13337

async def async_input():
    msg = await aioconsole.ainput("Quelle message veut tu envoyer ?")
    conn.send(msg.encode())
    
async def async_receive():
    msg = await conn.(1024)
    print(msg.decode())
    
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect((ip, port))

conn.send("Hello".encode())
entry = conn.recv(1024)
print(entry.decode())

while True:
    try :
        async_input()
        async_receive()
    except Exception:
        conn.close()
        raise (Exception) 