from tkinter import *
from quitter import Quitter


fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())


def makeform(root, fields):
    form = Frame(master=root)
    left = Frame(master=form)
    right = Frame(master=form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    right.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    for field in fields:
        label = Label(master=left, width=5, text=field)
        entry = Entry(master=right)
        label.pack(side=TOP)
        entry.pack(side=TOP, fill=X)
        '''
        StringVar() lets us extract values from Entry() forms
        after widget.destroy() method
        '''
        var = StringVar()
        entry.config(textvariable=var)
        var.set('Enter here')
        variables.append(var)

    return variables


if __name__ == '__main__':
    root = Tk()
    vars_ = makeform(root, fields)
    Button(master=root, text='Fetch',
           command=(lambda: fetch(vars_))).pack(side=LEFT)
    Quitter(master=root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars_)))
    root.mainloop()
