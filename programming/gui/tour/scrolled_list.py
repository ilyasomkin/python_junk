from tkinter import *


class ScrolledList(Frame):
    def __init__(self, options, master=None, cnf={}, **kw):
        super(ScrolledList, self).__init__(master, cnf, **kw)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index) # label = self.listbox.get(ACTIVE)
        self.runCommand(label)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list_ = Listbox(self, relief=SUNKEN)
        sbar.config(command=list_.yview)
        list_.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list_.pack(side=LEFT, expand=YES, fill=BOTH)
        for label in options:
            list_.insert(END, label)
        list_.bind('<Double-1>', self.handleList)
        self.listbox = list_

    def runCommand(self, selection):
        print('You selected', selection)


if __name__ == '__main__':
    options = (('Lumberjack-%s' % x) for x in range(20))
    ScrolledList(options).mainloop()
        