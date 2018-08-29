from tkinter import *
from tkinter.messagebox import showerror
import shelve


class PeopleGUI(Frame):
    fetchedBy_fieldname = 'key'
    fieldnames = ('name', 'age', 'job', 'pay')
    entries = {}

    def __init__(self, master=None):
        super(PeopleGUI, self).__init__(master)
        self.pack()
        self.create_widgets()
        self.entries[self.fetchedBy_fieldname].bind('<Key-Return>',
                                                    self.fetchRecord)

    def create_widgets(self):
        for (index, field) in enumerate((self.fetchedBy_fieldname,) +
                                        self.fieldnames):
            label = Label(self, text=field)
            entry = Entry(self)
            label.grid(row=index, column=0)
            entry.grid(row=index, column=1)
            self.entries[field] = entry

        Button(self.master, text='fetch',
               command=self.fetchRecord).pack(side=LEFT)
        Button(self.master, text='update',
               command=self.updateRecord).pack(side=LEFT)
        Button(self.master, text='quit',
               command=self.master.quit).pack(side=RIGHT)
        Button(self.master, text='clear',
               command=self.clearRecord).pack(side=RIGHT)

    def fetchRecord(self, event=None):
        key = self.entries[self.fetchedBy_fieldname].get()
        try:
            record = db[key]
        except Exception:
            showerror(title='Error', message='No such key: ' + key)
        else:
            for field in self.fieldnames:
                self.entries[field].delete(0, END)
                self.entries[field].insert(0, repr(getattr(record,
                                                           field)))

    def updateRecord(self):
        key = self.entries[self.fetchedBy_fieldname].get()
        if key in db:
            record = db[key]
        else:
            from person import Person
            record = Person(name='?', age='?')

        for field in self.fieldnames:
            setattr(record, field, eval(self.entries[field].get()))

        db[key] = record

    def clearRecord(self):
        for field in (self.fetchedBy_fieldname,) + self.fieldnames:
            self.entries[field].delete(0, END)


if __name__ == '__main__':
    db_filename = 'persondb'
    db = shelve.open(db_filename)
    root = Tk()
    root.title('People Shelve')
    app = PeopleGUI(master=root)
    root.mainloop()
    db.close()
