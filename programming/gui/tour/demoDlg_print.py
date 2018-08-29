from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, master=None, **options):
        super(Demo, self).__init__(master, **options)
        self.pack()
        Label(master=self, text='Basic demos').pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(master=self, text=key, command=func).pack(side=TOP,
                                                              fill=BOTH)
        Quitter(master=self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns =>', demos[name]())


if __name__ == '__main__':
    Demo().mainloop()
