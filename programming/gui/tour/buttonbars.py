from tkinter import *


class Checkbar(Frame):
    def __init__(self, master=None, picks=[], side=LEFT, anchor=W, cnf={}, **kw):
        super(Checkbar, self).__init__(master, cnf={}, **kw)
        self.vars_ = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(master=self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars_.append(var)

    def state(self):
        return [var.get() for var in self.vars_]


class Radiobar(Frame):
    def __init__(self, master=None,
                 picks=[], side=LEFT, anchor=W, cnf={}, **kw):
        super(Radiobar, self).__init__(master, cnf={}, **kw)
        self.var = StringVar()
        self.var.set(picks[0])
        for pick in picks:
            rad = Radiobutton(master=self, text=pick,
                              value=pick, variable=self.var)
            rad.pack(side=side, anchor=anchor, expand=YES)

    def state(self):
        return self.var.get()


if __name__ == '__main__':
    root = Tk()
    lng = Checkbar(root, ['Python', 'C#', 'Java', 'C++'])
    gui = Radiobar(root, ['win', 'x11', 'mac'], side=TOP, anchor=NW)
    tgl = Checkbar(root, ['All'])

    gui.pack(side=LEFT, fill=Y)
    lng.pack(side=TOP, fill=X)
    tgl.pack(side=LEFT)
    lng.config(relief=GROOVE, bd=2)
    gui.config(relief=RIDGE, bd=2)


    def allstates():
        print(gui.state(), lng.state(), tgl.state())


    from quitter import Quitter
    Quitter(master=root).pack(side=RIGHT)
    Button(master=root, text='Peek', command=allstates).pack(side=RIGHT)
    root.mainloop()
