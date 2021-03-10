"""













this is the server
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('starting server...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
