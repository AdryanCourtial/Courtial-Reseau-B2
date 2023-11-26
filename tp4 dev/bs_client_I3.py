import socket
import sys
import time
import re

host = '10.1.1.11' # IP du serveur
port = 13336       # Port choisir par le serveur

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try :

    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    time.sleep(2)

    answer = input("Que veux-tu envoyer au serveur ?")

    # p = re.compile("meo|waf")
    # if type(answer) is not str:
    #     raise TypeError(b"Ecrit une une phrase !")
    # elif p.match(answer == None):
    #     raise TypeError(b"Tu n'es pas le bienvenue Ici.")
    # else:
    
    s.send(answer.encode())

    
    data = s.recv(512)
    print(data)

except Exception as e:
    print(f"{e}")

sys.exit()