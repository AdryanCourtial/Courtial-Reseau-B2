import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('10.1.1.11', 13337))

s.listen(1)
conn, addr = s.accept()

while True: 
    try:
        request = conn.recv(1).decode

        if "/ GET" in request:
            print("HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>")
    except socket.error:
        print("Error Occured.")
        break

 

conn.close()