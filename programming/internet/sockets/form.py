from tkinter import *


entrysize = 40


class Form:
    def __init__(self, labels, master=None):
        labelsize = max(len(x) for x in labels) + 2
        box = Frame(master)
        box.pack(expand=YES, fill=X)
        rows = Frame(box, bd=2, relief=GROOVE)
        rows.pack(side=TOP, expand=YES, fill=X)
        self.content = {}
        for label in labels:
            row = Frame(rows)
            row.pack(fill=X)
            Label(row, text=label, width=labelsize).pack(side=LEFT)
            entry = Entry(row, width=entrysize)
            entry.pack(side=RIGHT, expand=YES, fill=X)
            self.content[label] = entry
        Button(box, text='Cancel', command=self.onCancel).pack(side=RIGHT)
        Button(box, text='Submit', command=self.onSubmit).pack(side=RIGHT)
        box.master.bind('<Return>', (lambda event: self.onSubmit()))

    def onSubmit(self):
        for key in self.content:
            print(key, '\t=>\t', self.content[key].get())

    def onCancel(self):
        Tk().quit()


class DynamicForm(Form):
    def __init__(self, labels=None):
        labels = input('Enter field names: ').split()
        super(DynamicForm, self).__init__(labels)

    def onSubmit(self):
        print('Field values...')
        super(DynamicForm, self).onSubmit()
        self.onCancel()


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        Form(['Name', 'Age', 'Job'])
    else:
        DynamicForm()
    mainloop()
