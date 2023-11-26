import socket
import sys
import time

host = '10.1.1.11' # IP du serveur
port = 13336       # Port choisir par le serveur

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try :

    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    time.sleep(2)
    answer = input("Que veux-tu envoyer au serveur ?")
    print(bytes(answer, 'utf-8'))
    s.sendall(answer)

except Exception as e:
    print(f"{e}")

sys.exit()