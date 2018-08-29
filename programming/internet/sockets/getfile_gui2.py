import getfile
from tkinter import *
from tkinter.messagebox import showinfo


def onSubmit():
    getfile.client(content['Server'].get(),
                   int(content['Port'].get()),
                   content['File'].get())
    showinfo('getfilegui-2', 'Download complete')


box = Tk()
labels = ['Server', 'Port', 'File']
content = {}
for (row, label) in enumerate(labels):
    Label(box, text=label).grid(column=0, row=row)
    entry = Entry(box)
    entry.grid(column=1, row=row, sticky=E + W)
    content[label] = entry

box.columnconfigure(0, weight=0)
box.columnconfigure(1, weight=1)
Button(text='Submit', command=onSubmit).grid(
    row=row + 1, column=0, columnspan=2)

box.title('getfilegui-2')
box.bind('<Return>', (lambda event: onSubmit()))
mainloop()
