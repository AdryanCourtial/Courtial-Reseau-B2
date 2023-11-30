import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.1.11', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        header = conn.recv(4)

        if not header: break

        header = header.decode()
        print(f"Tu dois lire les {int(header)} prochains Bytes")

        data = conn.recv(header)
        data = data.decode()
        print(data)
        res  = eval(data)
        conn.send(str(res).encode())

         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
