from tkinter import *
from quitter import Quitter


fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())



def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        label = Label(row, width=5, text=field)
        entry = Entry(row)
        row.pack(side=TOP, fill=X)
        label.pack(side=LEFT)
        entry.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(entry)
    return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents)))
    Button(root, text='Fetch',
    command=(lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()
