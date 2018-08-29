from tkinter import *
from gui6 import Hello


class HelloContainer(Frame):
    def __init__(self, master=None):
        super(HelloContainer, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        Hello(master=self).pack(side=RIGHT)
        Button(master=self, text='Attach', command=self.quit).pack(side=LEFT)


if __name__ == '__main__':
    HelloContainer().mainloop()
