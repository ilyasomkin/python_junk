from tkinter import *


root = Tk()
root.title('Example GUI')
widget = Label(master=root)
widget.config(text='Hello GUI World!')
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
