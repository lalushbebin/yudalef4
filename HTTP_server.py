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
        self.wfile.write('<h1>Erel - (Avni)</h1>'.encode())
        self.wfile.write('<img src="https://www.google.com/search?q=dum+cat&tbm=isch&ved=2ahUKEwjn1MTTj66EAxXTSaQEHZh_DnUQ2-cCegQIABAA&oq=dum+cat&gs_lp=EgNpbWciB2R1bSBjYXQyBxAAGIAEGBMyCBAAGAcYHhgTMggQABgHGB4YEzIIEAAYBxgeGBMyCBAAGAcYHhgTMggQABgHGB4YEzIIEAAYBxgeGBMyCBAAGAcYHhgTMggQABgHGB4YEzIIEAAYBxgeGBNIxhhQ2xJYhhRwAHgAkAEAmAGGAaABjQSqAQMwLjS4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ8ICChAAGIAEGIoFGEPCAgYQABgHGB6IBgE&sclient=img&ei=q2vOZafTPNOTkdUPmP-5qAc&bih=953&biw=1920#imgrc=kCP8xpKid2CIJM&imgdii=VQv9YndSVheILM">'.encode())

    # this is the object which take port


if __name__ == '__main__':
    server = HTTPServer(("", 8080), GFG)

    try:
        print("Server is running on http://127.0.0.1:8080/")
        server.serve_forever()
    except Exception as e:
        print(e)