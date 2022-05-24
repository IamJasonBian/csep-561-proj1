""" A very basic stdlib http server

    Serves files out of the current working directory. Credit to updating for
    python3 to Chris Gunn<cwize1@cs.washington.edu>.
"""
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 80

class Handler(SimpleHTTPRequestHandler):
    # Disable logging DNS lookups
    def address_string(self):
        return str(self.client_address[0])

httpd = HTTPServer(("", PORT), Handler)
print("Server1: httpd serving at port", PORT)
httpd.serve_forever()
