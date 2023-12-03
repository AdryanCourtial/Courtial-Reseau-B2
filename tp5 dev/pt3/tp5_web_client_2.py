import http.client

server_address = "10.1.1.11"
server_port = 13337

conn = http.client.HTTPConnection(server_address, server_port)

request = input("Quelle page voulais vous ?")
# Envoyer une requête GET au serveur
conn.request("GET", request)

# Récupérer la réponse du serveur
response = conn.getresponse()

print(f"Version: {response.version}")

# Afficher le code d'état de la réponse
print(f"Code d'état: {response.status}")

# Afficher le contenu de la réponse
print("Contenu de la réponse:")
print(response.read().decode())

# Fermer la connexion
conn.close()