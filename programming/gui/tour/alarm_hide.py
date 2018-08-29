from tkinter import *
import alarm


class Alarm(alarm.Alarm):
    def __init__(self, master=None, msecs=1000, cnf={}, **kw):
        self.shown = False
        super(Alarm, self).__init__(master, msecs, cnf, **kw)

    def repeater(self):
        self.bell()
        if self.shown:
            self.stopper.pack_forget()
        else:
            self.stopper.pack()
        self.shown = not self.shown
        self.after(self.msecs, self.repeater)


if __name__ == '__main__':
    Alarm(msecs=1000).mainloop()
