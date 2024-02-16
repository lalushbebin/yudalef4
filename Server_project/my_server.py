# importing all the functions 
# from http.server module 
from http.server import *

# creating a class for handling
# basic Get and Post Requests 
class MyServer(BaseHTTPRequestHandler):

    connected = 0
    # creating a function for Get Request
    def do_GET(self):
        MyServer.connected += 0.5
        # Success Response --> 200
        self.send_response(200)

        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # what we write in this function it gets visible on our
        # web-server
        file = open(r'web_server.html')
        self.wfile.write(file.read().encode())
        file.close()

    # this is the object which take port


# number and the server-name
# for running the server 
port = HTTPServer(('', 5555), MyServer)

# this is used for running our 
# server as long as we wish 
# i.e. forever 
port.serve_forever() 
