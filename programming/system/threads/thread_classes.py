import threading


numthreads = 5


class MyThread(threading.Thread):
    def __init__(self, id, count, mutex):
        threading.Thread.__init__(self)
        self.id = id
        self.count = count
        self.mutex = mutex

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.id, i))


stdout_mutex = threading.Lock()
threads = []

for i in range(numthreads):
    thread = MyThread(i, numthreads, stdout_mutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('Main thread exiting')
