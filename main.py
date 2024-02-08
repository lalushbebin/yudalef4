"""# importing all the functions
# from http.server module
from http.server import *

# Global variable to store the count
visit_count = 0
# creating a class for handling
# basic Get and Post Requests
class GFG(BaseHTTPRequestHandler):
    # creating a function for Get Request
    def do_GET(self):
        global visit_count  # Access the global variable

        # Increment the visit count for each GET request
        visit_count += 1
        # Success Response --> 200
        self.send_response(200)

        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # what we write in this function it gets visible on our
        # web-server
        self.wfile.write('<h1>OrWebsite</h1>'.encode())
        self.wfile.write('<h2>NeverGonnaGiveYouUp</h2>'.encode())
        self.wfile.write('<p>Visit Count: {visit_count}</p>'.encode())

    # this is the object which take port


'visit_count = 0'
# number and the server-name
# for running the server
port = HTTPServer(('', 5555), GFG)

# this is used for running our
# server as long as we wish
# i.e. forever
port.serve_forever()"""

from http.server import *

# Global variable to store the count
visit_count = 0

class GFG(BaseHTTPRequestHandler):
    def do_GET(self):

        global visit_count  # Access the global variable

        # Increment the visit count for each GET request
        visit_count += 1

        # Success Response --> 200
        self.send_response(200)

        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # Display the visit count on the website
        response = f'<h1>Or Harlys Website</h1><p>Visit Count: {visit_count}</p>'
        self.wfile.write(response.encode())

# Set the initial visit count to 0
visit_count = 0

# This is the object which takes port
# number and the server-name
# for running the server
port = HTTPServer(('', 5555), GFG)

# This is used for running our
# server as long as we wish
# i.e. forever
port.serve_forever()

