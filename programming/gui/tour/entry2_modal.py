from tkinter import *
from entry2 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries)
    popup.destroy()


def ask():
    popup = Toplevel()
    entries = makeform(popup, fields)
    Button(master=popup, text='OK',
           command=(lambda: show(entries, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()


root = Tk()
Button(master=root, text='Dialog', command=ask).pack()
root.mainloop()
