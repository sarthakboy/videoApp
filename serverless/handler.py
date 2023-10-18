from http.server import BaseHTTPRequestHandler
import http.server

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open("public/index.html", "rb") as f:
            self.wfile.write(f.read())

if __name__ == '__main__':
    PORT = 3000  # Choose your desired port
    httpd = http.server.HTTPServer(('0.0.0.0', PORT), Handler)
    print(f'Serving at port {PORT}')
    httpd.serve_forever()
