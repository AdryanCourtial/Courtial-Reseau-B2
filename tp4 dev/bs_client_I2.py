import socket
import sys
import time

host = '10.1.1.11' # IP du serveur
port = 13337       # Port choisir par le serveur

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try :

    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    time.sleep(2)
    answer = input("Que veux-tu envoyer au serveur ?")
    s.send(answer.encode())
    
    data = s.recv(512).decode()
    print(data)

except Exception as e:
    print(f"{e}")

sys.exit()