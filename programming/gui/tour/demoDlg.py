from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(Demo, self).__init__(master, cnf={}, **kw)
        self.pack()
        Label(master=self, text='Basic demos').pack()
        for (key, value) in demos.items():
            Button(master=self, text=key, command=value).pack(side=TOP,
                                                              fill=BOTH)
        Quitter(master=self).pack(side=TOP, fill=BOTH)


if __name__ == '__main__':
    Demo().mainloop()
