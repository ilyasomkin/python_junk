import _thread
import queue
import time


dataQueue = queue.Queue()


def producer(id_):
    for i in range(5):
        time.sleep(.1)
        print('put')
        dataQueue.put('[producer id_=%d, count=%d]' % (id_, i))


def consumer(root):
    try:
        print('get')
        data = dataQueue.get(block=False)
    except queue.Empty:
        pass
    else:
        root.insert('end', 'consumer got => %s\n' % str(data))
        root.see('end')
    root.after(250, lambda: consumer(root))


def makethreads():
    for i in range(4):
        _thread.start_new_thread(producer, (i,))


if __name__ == '__main__':
    from tkinter.scrolledtext import ScrolledText
    root = ScrolledText()
    root.pack()
    root.bind('<Button-1>', lambda event: makethreads())

    consumer(root)
    root.mainloop()
