import http.client

# Spécifier l'adresse et le port du serveur auquel vous souhaitez vous connecter
server_address = "10.1.1.11"
server_port = 13337

# Créer une connexion HTTP avec le serveur
conn = http.client.HTTPConnection(server_address, server_port)

# Spécifier le chemin de la ressource que vous souhaitez récupérer (dans cet exemple, la racine '/')
resource_path = '/'

# Envoyer une requête GET au serveur
conn.request("GET", resource_path)

# Récupérer la réponse du serveur
response = conn.getresponse()

# Afficher le code d'état de la réponse
print(f"Code d'état: {response.status}")

# Afficher le contenu de la réponse
print("Contenu de la réponse:")
print(response.read().decode('utf-8'))

# Fermer la connexion
conn.close()