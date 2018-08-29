from tkinter import *
from tkinter.messagebox import askokcancel


class Quitter(Frame):
    def __init__(self, master=None):
        super(Quitter, self).__init__(master)
        widget = Button(master=self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        answer = askokcancel('Verify exit', 'Really quit?')
        if answer:
            super(Quitter, self).quit()


if __name__ == '__main__':
    Quitter().mainloop()
