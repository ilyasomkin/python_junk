from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename
from quitter import Quitter
from scrolled_text import ScrolledText


class SimpleEditor(ScrolledText):
    def __init__(self, master=None, file=None, cnf={}, **kw):
        super(SimpleEditor, self).__init__(master, file=file)
        frame = Frame(master)
        frame.pack(fill=X)
        Button(frame, text='Save', command=self.onSave).pack(side=LEFT)
        Button(frame, text='Cut', command=self.onCut).pack(side=LEFT)
        Button(frame, text='Paste', command=self.onPaste).pack(side=LEFT)
        Button(frame, text='Find', command=self.onFind).pack(side=LEFT)
        Quitter(frame).pack(side=LEFT)
        self.text.config(font=('courier', 9, 'normal'))

    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()
            open(filename, 'w').write(alltext)

    def onCut(self):
        try:
            text = self.text.get(SEL_FIRST, SEL_LAST)
            self.text.delete(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)
        except TclError:
            pass

    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass

    def onFind(self):
        target = askstring('Simple Editor', 'Search string?')
        if target:
            where = self.text.search(target, INSERT, END)
            if where:
                print(where)
                pastit = where + ('+%dc' % len(target))
                # self.text.tag_remove(SEL, '1.0', END)
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop()
    else:
        SimpleEditor().mainloop()
