from tkinter import *


def greeting():
    print('Hello stdout world!..')


root = Tk()
root.title('GUI4.py')
win = Frame(master=root)
win.pack()

Button(master=win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
Label(master=win, text='Hello container world').pack(side=TOP)
Button(master=win, text='Quit', command=win.quit).pack(side=RIGHT)

root.mainloop()
