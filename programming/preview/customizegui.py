from tkinter import *
from tkinter.messagebox import showinfo
from tkinter102 import MyGUI


class CustomGUI(MyGUI):
    def reply(self):
        showinfo(title='popup', message='Ouch!')


if __name__ == '__main__':
    CustomGUI().pack()
    mainloop()
