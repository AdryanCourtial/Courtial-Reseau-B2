# Importer le module http.server
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Spécifier le port sur lequel le serveur écoutera
port = 8000

# Créer une instance de SimpleHTTPRequestHandler
handler = SimpleHTTPRequestHandler

# Créer une instance de TCPServer liée à l'adresse locale et au port spécifié
httpd = TCPServer(("localhost", port), handler)

# Afficher un message pour indiquer que le serveur est en cours d'exécution
print(f"Serveur en cours d'exécution sur le port {port}")

# Lancer le serveur
httpd.serve_forever()