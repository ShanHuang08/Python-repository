#!/usr/bin/python

"""
Function:
    You can use this program to test HTTP(S) GET and POST methods.

Usage:
    First of all, please go get the certificate file, 'server.pem'.
    It resides in your source code path:
        Web_Server/httpd/server.pem
    Then copy it into the folder where this program, "simple_python_http_server.py"
    reisides.

    3 kinds of operation:
        1. Run it with specified protocol (http or https) and specified port
        >>> sudo python simple_python_http_server.py https 987
        Serving at https://${YOUR_PC_IP}:987

        2. Run it ONLY with specified protocol (http or https), it will be run
           on respective default port
            2-1. HTTPS/443
            >>> sudo python simple_python_http_server.py https
            Serving at https://${YOUR_PC_IP}:443

            2-2. HTTP/80
            >>> sudo python simple_python_http_server.py http
            Serving at http://${YOUR_PC_IP}:80

        3. simply run without any argument, it will run on basic HTTP/80
        >>> sudo python simple_python_http_server.py
        Serving at http://${YOUR_PC_IP}:80
"""

import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import commands
import logging
import cgi
import sys
import ssl

PROTOCOL = 'http' # default is http
PORT     = 80     # default is 80
INTF     = commands.getoutput ("/sbin/ifconfig").split ("\n")[1].split ()[1][5:]

ARGV_LEN = len(sys.argv)
print('argv len:', ARGV_LEN)
for i in range(ARGV_LEN):
    print('argv %d: %s' % (i, str (sys.argv[i])))
print('')

if ARGV_LEN == 3:
    PROTOCOL = sys.argv[1]
    PORT     = int (sys.argv[2])
elif ARGV_LEN == 2:
    PROTOCOL = sys.argv[1]
    if PROTOCOL == 'https':
        PORT = 443

if PROTOCOL != 'http' and PROTOCOL != 'https':
    print('Protocol chosen error, you are using: %s' % (PROTOCOL))
    sys.exit (1)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("======= GET STARTED =======")
        logging.warning (self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET (self)

    def do_POST(self):
        print("======= POST STARTED =======")
        print(self.headers)
        form = cgi.FieldStorage (
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        print("======= POST VALUES =======")
        print(type(form))
        print(form)
        #for item in form.list:
        #    print item
        print("\n")
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET (self)

Handler = ServerHandler
SocketServer.ThreadingTCPServer.allow_reuse_address = True
if PROTOCOL == 'http':
    httpd = SocketServer.TCPServer ((INTF, PORT), Handler)
elif PROTOCOL == 'https':
    httpd = BaseHTTPServer.HTTPServer((INTF, PORT), Handler)
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)

print("Serving at: %(protocol)s://%(interface)s:%(port)s" % '\\')
dict(protocol=PROTOCOL, interface=INTF or "localhost", port=PORT)
httpd.serve_forever()
