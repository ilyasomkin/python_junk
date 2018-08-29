import sys
import time
import os
import time
from tkinter import *
from launchmodes import PortableLauncher
from gui.tools.windows import MainWindow


def runImmediate(mytools):
    print('Starting Python/Tk gadgets...')
    for (name, commandLine) in mytools:
        PortableLauncher(name, commandLine)()
    print('One moment please...')
    if sys.platform[:3] == 'win':
        for i in range(10):
            time.sleep(1)
            print('.' * 5 * (i + 1))


def runLauncher(mytools):
    root = MainWindow('PyGadgets PP4E')
    for (name, commandLine) in mytools:
        b = Button(root, text=name, fg='black', bg='beige', border=2,
                   command=PortableLauncher(name, commandLine))
        b.pack(side=LEFT, expand=YES, fill=BOTH)
    root.mainloop()


mytools = [
    ('PyEdit', 'Gui/TextEditor/textEditor.py'),
    ('PyCalc', 'Lang/Calculator/calculator.py'),
    ('PyPhoto', 'Gui/PIL/pyphoto1.py Gui/PIL/images'),
    ('PyMail', 'Internet/Email/PyMailGui/PyMailGui.py'),
    ('PyClock', 'Gui/Clock/clock.py -size 175 -bg white'
     ' -picture Gui/gifs/pythonPowered.gif'),
    ('PyToe', 'Ai/TicTacToe/tictactoe.py'
     ' -mode Minimax -fg white -bg navy'),
    ('PyWeb', 'LaunchBrowser.pyw'
     ' -live index.html www.rmi.net/~lutz')]


if __name__ == '__main__':
    prestart, toolbar = True, False
    if prestart:
        runImmediate(mytools)
    if toolbar:
        runLauncher(mytools)
