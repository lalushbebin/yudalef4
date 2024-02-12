import os

import http_server
import socketserver


if __name__ == '__main__':

    # directory = 'C:/networks/httpServerProject/http_web.html'
    # os.chdir(directory)

    # this is the object which take port
    # number and the server-name
    # for running the server
    port = http_server.HTTPServer(('127.0.0.1', 8000), http_server.GFG)
    # this is used for running ouipconfigr
    # server as long as we wish
    # i.e. forever
    port.serve_forever()
