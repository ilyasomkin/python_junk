from tkinter import *


win = Tk()
img = PhotoImage(file='logo.gif')
canvas = Canvas(win)
canvas.pack(fill=BOTH)
canvas.config(width=img.width(), height=img.height())
canvas.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
