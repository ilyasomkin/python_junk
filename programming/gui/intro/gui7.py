from tkinter import *


class HelloPackage:
    def __init__(self, master=None):
        self.top = Frame(master)
        self.top.pack()
        self.data = 0
        self.create_widgets()

    def create_widgets(self):
        Button(master=self.top, text='Bye',
               command=self.top.quit).pack(side=LEFT)
        Button(master=self.top, text='Hye',
               command=self.message).pack(side=RIGHT)

    def message(self):
        self.data += 1
        print('Hello number', self.data)


if __name__ == '__main__':
    HelloPackage().top.mainloop()
