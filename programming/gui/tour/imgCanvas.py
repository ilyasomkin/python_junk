from tkinter import *


win = Tk()
img = PhotoImage(file='logo.gif')
canvas = Canvas(win)
canvas.pack(fill=BOTH)
canvas.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
