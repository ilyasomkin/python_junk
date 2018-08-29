from tkinter import *
from tkinter102 import MyGUI


main_window = Tk()
Label(main_window, text=__name__).pack()


popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGUI(popup).pack(side=RIGHT)
main_window.mainloop()
