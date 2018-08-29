from tkinter import *


root = Tk()

for i in range(5):
    for j in range(4):
        label = Label(root, text='%d.%d' % (i, j), relief=RIDGE)
        label.grid(row=i, column=j, sticky=NSEW)
        root.rowconfigure(i, weight=1)
        root.columnconfigure(j, weight=1)

mainloop()
