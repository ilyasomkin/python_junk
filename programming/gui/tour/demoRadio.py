from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(Demo, self).__init__(master, cnf={}, **kw)
        self.pack()
        Label(master=self, text='Radio demos').pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(master=self, text=key,
                        command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(key)
        Button(master=self, text='State', command=self.report).pack(fill=X)
        Quitter(master=self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('You pressed', pick)
        print('Result:', demos[pick]())

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    Demo().mainloop()
