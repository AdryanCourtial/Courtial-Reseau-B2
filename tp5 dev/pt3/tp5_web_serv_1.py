from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

port = 13337
adress = "10.1.1.11"

handler = SimpleHTTPRequestHandler

httpd = TCPServer((adress, port), handler)

print(f"Serveur en cours d'exécution sur le port {port}")

# Lancer le serveur
httpd.serve_forever()

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Personnaliser la réponse pour la requête GET
        if self.path == '/':
            self.send_response(200)
            self.send_header("Reussi", "HTTP/1.0 200 OK\n\n<h1>Hello je suis un serveur HTTP</h1>")
            self.end_headers()
            self.wfile.write(b"Page d'accueil")