import sys
from socket import *


host = 'localhost'
port = 5009


def initListenerSocket(port=port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    return conn


def redirectOut(host=host, port=port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('w')
    sys.stdout = file
    return sock


def redirectIn(host=host, port=port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r')
    sys.stdin = file
    return sock


def redirectBothAsClient(host=host, port=port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    ofile = sock.makefile('w')
    ifile = sock.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return sock


def redirectBothAsServer(host=host, port=port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    ofile = conn.makefile('w')
    ifile = conn.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return conn
