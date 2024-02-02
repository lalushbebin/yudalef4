import json
import os
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

count = 0
code = "011FGH"

class GetPostServer(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, _server):
        self.args = {'count': 0}
        super().__init__(request, client_address, _server)

    def do_GET(self):
        global count
        if self.path == '/':
            self.path = '/index.html'

            # update the counter
            count += 1
            self.args['count'] = count

        if os.path.isfile('./public' + self.path):
            # handle a get request
            self.send_response(200)

            extension = self.path.split(".")[-1]

            if extension == 'js':
                self.send_header('content-type', 'text/javascript')
            else:
                self.send_header('content-type', 'text/' + extension)
            self.end_headers()

            with open('public' + self.path, 'r') as file:
                for key, argument in self.args.items():
                    self.wfile.write(file.read().replace("{{" + key + "}}", str(argument)).encode())
        else:
            self.send_response(404)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            with open('public/default.html', 'r') as file:
                self.wfile.write(file.read().replace("{{site_name}}", 'Error 404').encode())
            self.wfile.write("<h1>Url unreachable!</h1>".encode())
            self.wfile.write("</body></html>".encode())

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length)
        fields = json.loads(field_data)

        if fields['code'] == code:
            print("test")


if __name__ == '__main__':
    server = HTTPServer(("", 8080), GetPostServer)

    try:
        print("Server is running on http://127.0.0.1:8080/")
        server.serve_forever()
    except Exception as e:
        print(e)
