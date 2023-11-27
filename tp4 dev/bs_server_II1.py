import socket
import sys
import argparse

host = '10.1.1.11' # string vide signifie, dans ce conetxte, toutes les IPs de la machine
port = 13337 # choisi arbitrairement



#GERE LES ARGS
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", action="store",type=int, default=13337)
args = parser.parse_args()

if args.port < 0 or args.port > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    sys.exit(1) 
elif args.port > 0 and args.port < 1024:
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    sys.exit(2)
else:
    port = args.port 

#GERE LE SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  
s.listen(5) # 1 = Le Nombre de connexion Accpeter


conn, addr = s.accept()
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse
print(f"Un client vient de se co et son IP c'est {addr}.")



while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)
        data = data.decode()
        print(f"Données reçues du client : {data}")

        # On affiche dans le terminal les données reçues du client
        if 'meo' in data:
            conn.sendall(b'Meo a toi confrere.')
        elif 'waf' in data:
            conn.sendall(b'ptdr t ki')
        else :
            conn.sendall(b'Mes respects humble humain.')

        conn.close()
        sys.exit()


    except socket.error:
        print("Error Occured.")
        break

conn.close()
sys.exit()