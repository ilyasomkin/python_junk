import _thread, time


stdout_mutex = _thread.allocate_lock()
exit_mutexes = [_thread.allocate_lock() for i in range(5)]


def counter(id, count):
    for i in range(count):
        time.sleep(1)
        stdout_mutex.acquire()
        print('[%s] => %s' % (id, i))
        stdout_mutex.release()
    exit_mutexes[id].acquire()


for i in range(5):
    _thread.start_new_thread(counter, (i, 5))

for mutex in exit_mutexes:
    while not mutex.locked():
        pass

print('Main thread exiting')
