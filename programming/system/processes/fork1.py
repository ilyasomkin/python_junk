import os


def child():
    print('Hello from child', os.getpid())
    os._exit(0)


def parent():
    while True:
        newpid = os.fork()
        print('newpid:', newpid)
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break


parent()
