from tkinter import *


class Hello(Frame):
    def __init__(self, master=None):
        super(Hello, self).__init__(master)
        self.pack()
        self.data = 42
        self.create_widgets()

    def create_widgets(self):
        button = Button(master=self, text='Hello frame world!',
                        command=self.message)
        button.pack(side=LEFT)

    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)


if __name__ == '__main__':
    Hello().mainloop()
