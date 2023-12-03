import http.client

server_address = "10.1.1.11"
server_port = 13337

conn = http.client.HTTPConnection(server_address, server_port)


# Envoyer une requête GET au serveur
conn.request("GET", "/")

# Récupérer la réponse du serveur
response = conn.getresponse()

print(f"Code d'état: {response.version}")

# Afficher le code d'état de la réponse
print(f"Code d'état: {response.status}")

# Afficher le contenu de la réponse
print("Contenu de la réponse:")
print(response.read().decode('utf-8'))

# Fermer la connexion
conn.close()