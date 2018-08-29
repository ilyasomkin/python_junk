from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)


top = Tk()
top.title('Echo')

Label(top, text='Enter your name:').pack(side=TOP)
entry = Entry(top, text='spam')
entry.pack(side=TOP)
button = Button(top, text='Submit', command=(lambda: reply(entry.get())))
button.pack()

top.mainloop()
