from sys import exit
from tkinter import *
from gui6 import Hello


parent = Frame(master=None)
parent.pack()
Hello(master=parent).pack(side=RIGHT)

Button(master=parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
