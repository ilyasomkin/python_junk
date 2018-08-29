from tkinter import *
from glob import glob
import demoCheck
import random


gifdir = '/root/tools/SageMath/local/share/maxima/5.39.0/doc/html/figures'


class ButtonPicsDemo(Frame):
    def __init__(self, master=None, gifdir=gifdir, cnf={}, **kw):
        super(ButtonPicsDemo, self).__init__(master)
        self.pack()
        self.lbl = Label(self, text='None', bg='blue', fg='red')
        self.pix = Button(self, text='Press me', command=self.draw, bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        demoCheck.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob(gifdir + '/*.gif')
        self.images = [(x, PhotoImage(file=x)) for x in files]
        print(files)

    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)


if __name__ == '__main__':
    ButtonPicsDemo().mainloop()
