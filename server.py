import sys
import http.server
import socketserver
import urllib

server_side = sys.argv[1]

def server(port):
    port = int(port)
    handler = http.server.BaseHTTPRequestHandler
    httpd = socketserver.TCPServer(('', port), handler)
    print('serving at port ' + str(port))
    httpd.serve_forever()

def client(url, dest):
    urllib.urlretrieve(url, dest)

if __name__ == '__main__':
    if server_side == 'server':
        port = sys.argv[2]
        server(port)
    elif server_side == 'client':
        url = sys.argv[2]
        dest = sys.argv[3]
        client(url, dest)
    else:
        print('Error!')