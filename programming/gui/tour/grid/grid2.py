from tkinter import *


colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']


def gridbox(master):
    for (row, color) in enumerate(colors):
        label = Label(master, text=color, relief=RIDGE, width=25)
        entry = Entry(master, bg=color, relief=SUNKEN, width=50)
        label.grid(row=row, column=0)
        entry.grid(row=row, column=1)
        entry.insert(0, 'grid')


def packbox(master):
    for color in colors:
        row = Frame(master)
        label = Label(row, text=color, relief=RIDGE, width=25)
        entry = Entry(row, bg=color, relief=SUNKEN, width=50)
        row.pack(side=TOP)
        label.pack(side=LEFT)
        entry.pack(side=RIGHT)
        entry.insert(0, 'pack')


if __name__ == '__main__':
    root = Tk()
    gridbox(Toplevel())
    packbox(Toplevel())
    Button(root, text='Quit', command=root.quit).pack()
    mainloop()
