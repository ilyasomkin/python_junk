import os, time, queue
from multiprocessing import Process, Queue


class Counter(Process):
    label = ' @'
    def __init__(self, start, queue):
        super(Counter, self).__init__()
        self.state = start
        self.post = queue

    def run(self):
        for i in range(3):
            time.sleep(1)
            self.state += 1
            print(self.label, self.pid, self.state)
            self.post.put([self.pid, self.state])

        print(self.label, self.pid, '-')


if __name__ == '__main__':
    print('start', os.getpid())
    expected = 9

    post = Queue()
    p, q, r = Counter(0, post), Counter(100, post), Counter(1000, post)
    p.start(); q.start(); r.start()

    while expected:
        time.sleep(.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data')
        else:
            print('posted:', data)
            expected -= 1

    p.join(); q.join(); r.join()
    print('finish', os.getpid(), r.exitcode)
