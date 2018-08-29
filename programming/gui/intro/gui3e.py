from tkinter import *
import sys


def hello(event):
    print('Press twice to exit')


def quit(event):
    print('Hello, I must be going...')
    sys.exit()


widget = Button(master=None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.mainloop()
