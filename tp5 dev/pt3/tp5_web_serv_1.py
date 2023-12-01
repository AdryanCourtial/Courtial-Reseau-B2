import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.11', 13337))

s.listen(1)
conn, addr = s.accept()

while True: 
    try:
        request = conn.recv(1).decode
    except socket.error:
        print("Error Occured.")
        break

 

conn.close()