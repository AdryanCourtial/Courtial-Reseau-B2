import socket

ip = "10.1.1.11"
port = 13337

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect((ip, port))

conn.send("Hello".encode())
entry = conn.recv(1024)
print(entry.decode())

while True:
    try :
        pass
    except Exception:
        conn.close()
        raise (Exception) 