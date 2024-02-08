from http.server import *
import threading

count = 0.5

class GFG(BaseHTTPRequestHandler):
    def do_GET(self):
        global count
        count += 0.5
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        response = f'<h1>Welcome - (My first Http server)</h1>'
        response += f'<p style="color: red;">hi - (I love pizza)</p>'
        response += f'<p style="color: black;">members: {int(count)}</p>'
        self.wfile.write(response.encode())

if __name__ == '__main__':
    port = HTTPServer(('192.168.26.242', 5555), GFG)
    port.serve_forever()
