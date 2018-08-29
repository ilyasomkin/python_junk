import os, sys, time


filename = '/tmp/fifo_temp'


def child():
    pipeout = os.open(filename, os.O_WRONLY)
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent():
    pipein = open(filename, 'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got [%s] at %s' % (os.getpid(),
                                            line,
                                            time.time()))


if __name__ == '__main__':
    if not os.path.exists(filename):
        os.mkfifo(filename)
    if len(sys.argv) == 1:
        parent()
    else:
        child()
