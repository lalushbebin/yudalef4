# importing all the functions
# from http.server module
from http.server import *


# creating a class for handling
# basic Get and Post Requests
class GFG(BaseHTTPRequestHandler):

    # creating a function for Get Request
    def do_GET(self):
        # Success Response --> 200
        self.send_response(200)

        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # what we write in this function it gets visible on our
        # web-server
        self.wfile.write('<h1>Osher - (Levi)</h1>'.encode())
        self.wfile.write('<img src="https://tabakor.co.il/wp-content/uploads/2022/08/Mac-Baren-Cool-Mint-Choice-%D7%9E%D7%A7-%D7%91%D7%A8%D7%9F-%D7%9E%D7%A0%D7%98%D7%94-%D7%A7%D7%A8%D7%99%D7%A8%D7%94.png">'.encode())

    # this is the object which take port


if __name__ == '__main__':
    server = HTTPServer(("", 8080), GFG)

    try:
        print("Server is running on http://127.0.0.1:8080/")
        server.serve_forever()
    except Exception as e:
        print(e)
