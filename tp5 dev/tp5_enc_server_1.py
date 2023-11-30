import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.1.11', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        header = conn.recv(1)

        if not header: break

        header_len = int.from_bytes(header[0:1], byteorder='big')
        print(f"Tu dois lire les {header_len} prochains Bytes")

        chunks = []

        br = 0

        while br < header_len:
            chunk = conn.recv(min(header_len - br,
                                1024))
            if not chunk:
                raise RuntimeError('Invalid chunk received bro')

        # on ajoute le morceau de 1024 ou moins à notre liste
            chunks.append(chunk)

        # on ajoute la quantité d'octets reçus au compteur
            br += len(chunk)

    # ptit one-liner pas combliqué à comprendre pour assembler la liste en un seul message
        message_received = b"".join(chunks).decode('utf-8')
        print(f"Received from client {message_received}")
        conn.send(message_received.encode())



         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
