from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.scrolledtext import ScrolledText


class GuiOutput:
    font = ('courier', 9, 'normal')

    def __init__(self, master=None):
        self.text = None
        if master:
            self.popupnow(master)

    def popupnow(self, master=None):
        if self.text:
            return
        self.text = ScrolledText(master or Toplevel())
        self.text.config(font=self.font)
        self.text.pack()

    def write(self, text):
        self.popupnow()
        self.text.insert(END, str(text))
        self.text.see(END)
        self.text.update()

    def writelines(self, lines):
        for line in lines:
            self.write(line)


class GuiInput:
    def __init__(self):
        self.buff = ''

    def inputLine(self):
        line = askstring('GuiInput', 'Enter input line + <crlf> (cancel=eof)')
        if line == None:
            return ''
        else:
            return line + '\n'

    def read(self, bytes_=None):
        if not self.buff:
            self.buff = self.inputLine()
        if bytes_:
            text = self.buff[:bytes_]
            self.buff = self.buff[bytes_:]
        else:
            text = ''
            line = self.buff
            while line:
                text = text + line
                line = self.inputLine()
        return text

    def readline(self):
        text = self.buff or self.inputLine()
        self.buff = ''
        return text

    def readlines(self):
        lines = []
        while True:
            next = self.readline()
            if not next:
                break
            lines.append(next)
        return lines


def redirectedGuiFunc(func, *pargs, **kwargs):
    import sys
    saveStreams = sys.stdin, sys.stdout
    sys.stdin = GuiInput()
    sys.stdout = GuiOutput()
    sys.stderr = sys.stdout
    result = func(*pargs, **kwargs)
    sys.stdin, sys.stdout = saveStreams
    return result


def redirectedGuiShellCmd(command):
    import os
    input = os.popen(command, 'r')
    output = GuiOutput()

    def reader(input, output):
        while True:
            line = input.readline()
            if not line:
                break
            output.write(line)
    reader(input, output)


if __name__ == '__main__':
    def makeUpper():
        while True:
            try:
                line = input('Line? ')
            except:
                break
            print(line.upper())
        print('end of file')

    def makeLower(input, output):
        while True:
            line = input.readline()
            if not line:
                break
            output.write(line.lower())
        print('end of file')

    root = Tk()
    Button(root, text='test streams',
           command=lambda: redirectedGuiFunc(makeUpper)).pack(fill=X)
    Button(root, text='test files  ',
           command=lambda: makeLower(GuiInput(), GuiOutput())).pack(fill=X)
    Button(root, text='test popen  ',
           command=lambda: redirectedGuiShellCmd('ls -la')).pack(fill=X)
    root.mainloop()
