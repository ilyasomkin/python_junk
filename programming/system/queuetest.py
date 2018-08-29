import _thread, queue, time


numconsumers = 2
numproducers = 4
nummessages = 4

stdout_mutex = _thread.allocate_lock()

dataQueue = queue.Queue()


def producer(id):
    for msg in range(nummessages):
        time.sleep(id)
        dataQueue.put('[producer id = %d, count = %d]' % (id, msg))


def consumer(id):
    while True:
        time.sleep(.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with stdout_mutex:
                print('consumer', id, 'got =>', data)


if __name__ == '__main__':
    for i in range(numconsumers):
        _thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        _thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers - 1) * nummessages) + 1)
    print('Main thread exiting')
