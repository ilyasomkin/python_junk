import os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '/root/python/Python programming/preview'
port = 80

os.chdir(webdir)
srvaddr = ('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()
