import os, time, threading


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz + .1)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(),
                                            line.decode(),
                                            time.time()))


pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)
