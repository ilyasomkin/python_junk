import threading
import queue
import time

from tkinter.scrolledtext import ScrolledText


class ThreadGui(ScrolledText):
    threadsPerClick = 4

    def __init__(self, master=None):
        super(ThreadGui, self).__init__(master)
        self.pack()
        self.dataQueue = queue.Queue()
        self.bind('<Button-1>', self.makethreads)
        self.consumer()

    def producer(self, id_):
        for i in range(5):
            time.sleep(0.1)
            self.dataQueue.put('[producer id_=%d, count=%d]' % (id_, i))

    def consumer(self):
        try:
            data = self.dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            self.insert('end', 'consumer got => %s\n' % str(data))
            self.see('end')
        self.after(100, self.consumer)

    def makethreads(self, event):
        for i in range(self.threadsPerClick):
            threading.Thread(target=self.producer, args=(i,)).start()


if __name__ == '__main__':
    root = ThreadGui()
    root.mainloop()
