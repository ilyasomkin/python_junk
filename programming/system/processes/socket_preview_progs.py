from socket_preview import client, server
import os, sys
from threading import Thread


try:
    mode = int(sys.argv[1])
except Exception as e:
    print('Error:', e)
    sys.exit(1)
else:
    if mode == 1:
        server()
    elif mode == 2:
        client('client: process = %s' % os.getpid())
    else:
        for i in range(5):
            Thread(target=client, args=('client: thread = %s' % i,)).start()
