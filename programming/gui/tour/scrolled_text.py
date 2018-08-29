from tkinter import *


class ScrolledText(Frame):
    def __init__(self, master=None, text='', file=None, cnf={}, **kw):
        super(ScrolledText, self).__init__(master)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets()
        self.settext(text, file)

    def makeWidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def gettext(self):
        return self.text.get('1.0', END+'-1c')


if __name__ == '__main__':
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])
        root.title(sys.argv[1])
    else:
        st = ScrolledText(text='Words go here')
        root.title(st.gettext())


    def show(event):
        print(repr(st.gettext()))


    root.bind('<Key-Escape>', show)
    root.mainloop()
