from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 3000


class Server(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve files from the current directory
        super().do_GET()


# Set up an HTTP server
with socketserver.TCPServer(("", PORT), Server) as httpd:
    print(f"Servidor ejecutandose en el puerto {PORT}")
    httpd.serve_forever()
