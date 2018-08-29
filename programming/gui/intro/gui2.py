from tkinter import *
import sys


root = Tk()
button = Button(master=root, text='Hello widget world!', command=root.quit)
button.pack(expand=YES)
root.mainloop()
