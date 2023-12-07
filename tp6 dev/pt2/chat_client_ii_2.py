import socket
import sys

ip = "10.1.1.11"
port = 13337

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect((ip, port))

while True:
    try :
        conn.send("Hello".encode())

        entry = conn.recv(1024)
        print(entry.decode())

    except Exception:
        conn.close()
        raise Exception 
