import os


exit_count = 0


def child():
    global exit_count
    exit_count += 1
    print('Hello from child', os.getpid(), exit_count)
    os._exit(exit_count)
    print('Never reached')


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q':
                break


if __name__ == '__main__':
    parent()
