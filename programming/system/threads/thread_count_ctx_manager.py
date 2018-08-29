import _thread, time


stdout_mutex = _thread.allocate_lock()
numthreads = 5
exit_mutexes = [_thread.allocate_lock() for i in range(numthreads)]


def counter(id, count, mutex):
    for i in range(count):
        time.sleep(1 / (id + 1))
        '''
        __enter__ in 'with' block acquires a block for critical section
        __exit__ releases the last one.
        '''
        with mutex:
            print('[%s] => %s' % (id, i))
    exit_mutexes[id].acquire()


for i in range(numthreads):
    _thread.start_new_thread(counter, (i, numthreads, stdout_mutex))

while not all(mutex.locked() for mutex in exit_mutexes):
    time.sleep(.25)

print('Main thread exiting')
