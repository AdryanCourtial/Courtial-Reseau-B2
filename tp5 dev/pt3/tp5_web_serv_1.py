from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

port = 13337
adress = "10.1.1.11"

handler = SimpleHTTPRequestHandler

httpd = TCPServer((adress, port), handler)

print(f"Serveur en cours d'exécution sur le port {port}")

# Lancer le serveur
httpd.serve_forever()