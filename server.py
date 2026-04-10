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
        elif self.path == '/download/testing.html':
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="reader.html"')
            self.end_headers()
            with open('testing.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            super().do_GET()

if __name__ == "__main__":
    server_address = ('10.48.101.125', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Server running on http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()
    