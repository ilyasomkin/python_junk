from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(Demo, self).__init__(master, cnf={}, **kw)
        self.pack()
        self.tools()
        Label(master=self, text='Check demos').pack()
        self.vars_ = []
        for key in demos:
            var = IntVar()
            Checkbutton(master=self, text=key, variable=var,
                        command=demos[key]).pack(side=LEFT)
            self.vars_.append(var)

    def report(self):
        for var in self.vars_:
            print(var.get(), end=' ')
        print()

    def tools(self):
        frame = Frame(master=self)
        frame.pack(side=RIGHT)
        Button(master=frame, text='State',
               command=self.report).pack(fill=X)
        Quitter(master=frame).pack(fill=X)


if __name__ == '__main__':
    Demo().mainloop()
