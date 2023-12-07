import asyncio
import socket

ip = "10.1.1.11"
port = 13337

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(ip, port)

while True:
    try:

        conn.send("Hello".encode())
        
        conn.recv(1024)

    except Exception:
        conn.close()
        raise Exception


