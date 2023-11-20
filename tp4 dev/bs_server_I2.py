import socket
import sys

host = '10.1.1.11' # string vide signifie, dans ce conetxte, toutes les IPs de la machine
port = 13337  # port choisi arbitrairement

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  
s.listen(1) # 1 = Le Nombre de connexion Accpeter



conn, addr = s.accept()
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse
print(f"Un client vient de se co et son IP c'est {addr}.")


while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(512)

        # On affiche dans le terminal les données reçues du client
        if data.find("meo") != -1:
            print("Meo à toi confrère.")

        if data.find("waf") != -1:
            print("ptdr t ki")

        if data.find("waf") == -1 and data.find("meo") == -1 :
            print("Mes respects humble humain.")

        # On répond au client un truc
        conn.sendall(b'Hi mate !')
        conn.sendall(b'Hi mate !')
        conn.sendall(b'Hi mate !')


    except socket.error:
        print("Error Occured.")
        break

conn.close()
sys.exit()
