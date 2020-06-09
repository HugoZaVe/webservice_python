from http.server import SimpleHTTPRequestHandler, HTTPServer




def run(server_class, handler_class):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

a = HTTPServer
b = SimpleHTTPRequestHandler 

run(a ,b)