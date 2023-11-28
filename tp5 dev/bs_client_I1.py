import socket
import sys

# On définit la destination de la connexion
host = '10.1.1.11'  # IP du serveur
port = 13337      # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect((host, port))
# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

# Envoi de data bidon
s.send("10000")

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(512)

# On libère le socket TCP

# Affichage de la réponse reçue du serveur
 

sys.exit()
