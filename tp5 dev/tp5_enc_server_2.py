import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.1.11', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        signe = conn.recv(1) # JE RECUP EN PREMIER LE SIGNE 

        if not signe: break
        # VERIF POUR SAVOIR QUELLE SIGNE CES
        if signe.decode == 1:
            signe = "+"
        elif signe.decode == 2:
            signe = "-"
        elif signe.decode == 3:
            signe = "*"

        print(f"Le signe est {signe}")

        #BOUCLER POUR RECUP LES DEUX OP ET LES REMETTRE DANS LORDRE AVEC LE SIGNE 

        header1 = conn.recv(1)
        header1_len = int.from_bytes(header1[0:1], byteorder='big')
        print(f"Tu dois lire les {header1_len} prochains Bytes")

        chunks1 = []

        br = 0

        while br < header1_len:
            chunk1 = conn.recv(min(header1_len - br, 1024))

            if not chunk1:
                raise RuntimeError('Invalid chunk received bro')

            # on ajoute le morceau de 1024 ou moins à notre liste
            chunks1.append(chunk1)

            # on ajoute la quantité d'octets reçus au compteur
            br += len(chunk1)

        op1 = b"".join(chunks1).decode('utf-8')
        print(f"Received from client {op1}")



        header2 = conn.recv(1)
        header2_len = int.from_bytes(header2[0:1], byteorder='big')
        print(f"Tu dois lire les {header2_len} prochains Bytes")

        chunks2 = []

        br = 0

        while br < header2_len:
            chunk2 = conn.recv(min(header2_len - br, 1024))

            if not chunk2:
                raise RuntimeError('Invalid chunk received bro')

            # on ajoute le morceau de 1024 ou moins à notre liste
            chunks2.append(chunk2)

            # on ajoute la quantité d'octets reçus au compteur
            br += len(chunk2)    


        op2 = b"".join(chunks2).decode('utf-8')
        print(f"Received from client {op2}")

        if conn.recv(1) == "0".encode():
            print("gg fin de la partie 1 tu as bien recu le dernier bytes le clafin")

        res = eval(op1 + str(signe) + op2)
        conn.send(str(res).encode())

    except socket.error:
        print("Error Occured.")
        break

conn.close()