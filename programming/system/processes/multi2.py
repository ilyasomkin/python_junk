import os
from multiprocessing import Process, Pipe


def sender(pipe):
    print('sender pid:', os.getpid())
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()


def talker(pipe):
    print('talker pid:', os.getpid())
    pipe.send(dict(name='Bob', age=42))
    reply = pipe.recv()
    print('talker got:', reply)


if __name__ == '__main__':
    print('start pid:', os.getpid())
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd,)).start()

    print('parent got:', parentEnd.recv())
    parentEnd.close()

    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()
    print('parent got:', parentEnd.recv())
    parentEnd.send({x * 2 for x in 'spam'})
    child.join()
    print('parent exit')
