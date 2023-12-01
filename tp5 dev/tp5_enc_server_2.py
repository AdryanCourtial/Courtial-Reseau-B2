import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.1.11', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        signes = conn.recv(1) # JE RECUP EN PREMIER LE SIGNE 

        if not signes: break
        # VERIF POUR SAVOIR QUELLE SIGNE CES

        plus = 1
        moins = 2
        multiplier = 3

        if signes == plus.to_bytes(1, "big"):
            signe = "+"
        elif signes == moins.to_bytes(1, "big"):
            signe = "-"
        elif signes == multiplier.to_bytes(1, "big"):
            signe = "*"
        

        print(f"Le signe est {signe}")

        #BOUCLER POUR RECUP LES DEUX OP ET LES REMETTRE DANS LORDRE AVEC LE SIGNE 

        header1 = conn.recv(1)
        header1_len = int.from_bytes(header1, byteorder='big')

        print(f"Tu dois lire les {header1_len} prochains Bytes")

        op1 = conn.recv(header1_len)

        if not op1:
            raise RuntimeError('Invalid chunk received bro')
        print(f"Received from client {op1}")

        header2 = conn.recv(1)
        header2_len = int.from_bytes(header2, byteorder='big')

        op2 = conn.recv(header2_len)

        print(f"Received from client {op2}")

        if conn.recv(1) == "0".encode():
            print("gg fin de la partie 1 tu as bien recu le dernier bytes le clafin")

        op1 = int.from_bytes(op1, "big")
        op2 = int.from_bytes(op2, "big")
        print(signe)

        res = eval(str(op1) + signe + str(op2))
        conn.send(str(res).encode())   

    except socket.error:
        print("Error Occured.")
        break

conn.close()