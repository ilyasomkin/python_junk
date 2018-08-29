from tkinter import *
from quitter import Quitter


def fetch():
    print('Input =>', entry.get())


root = Tk()
entry = Entry(master=root)
entry.insert(0, 'Type here')
entry.pack(side=TOP, fill=X)

entry.focus()

entry.bind('<Return>', (lambda event: fetch()))
button = Button(master=root, text='Fetch', command=fetch)
button.pack(side=LEFT)
Quitter(master=root).pack(side=RIGHT)
root.mainloop()
