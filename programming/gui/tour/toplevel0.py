from tkinter import Toplevel, Button, Label
import sys


win1 = Toplevel()
win2 = Toplevel()

Button(master=win1, text='Spam', command=sys.exit).pack()
Button(master=win2, text='SPAM', command=sys.exit).pack()

Label(text='popup').pack()
win1.mainloop()
