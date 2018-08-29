from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(Demo, self).__init__(master, cnf={}, **kw)
        self.pack()
        Label(master=self, text='Scale demos').pack()
        self.var = IntVar()
        Scale(master=self, label='Pick demo number',
              command=self.onMove, variable=self.var,
              from_=0, to=len(demos) - 1).pack()
        Scale(master=self, label='Pick demo number',
              command=self.onMove, variable=self.var,
              from_=0, to=len(demos) - 1, length=200,
              tickinterval=1, showvalue=YES,
              orient='horizontal').pack()
        Quitter(master=self).pack(side=RIGHT)
        Button(master=self, text='Run demo',
               command=self.onRun).pack(side=LEFT)
        Button(master=self, text='State',
               command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        print('in onMove', value)

    def onRun(self):
        position = self.var.get()
        print('You picked', position)
        demo = list(demos.values())[position]

        print(demo())

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()
