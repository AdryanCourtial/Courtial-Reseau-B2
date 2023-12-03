import socket
import sys

host = '10.1.1.11' 
port = 13337 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  

s.listen(1)

conn, addr = s.accept()

while True: 
    try:
        request = conn.recv(1024).decode

        print(request)

        if "/ GET" in request:
            print("HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>")


    except socket.error:
        print("Error Occured.")
        break

 

conn.close()
sys.exit()