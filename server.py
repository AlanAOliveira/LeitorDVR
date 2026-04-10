from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('reader.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        self.wfile.write(html_content.encode('utf-8'))

    def do_GET(self):
        if self.path == '/testing':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('testing.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print("Server running on http://10.48.101.125:8000")
    httpd.serve_forever()
    