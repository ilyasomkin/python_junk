from tkinter import *
from gui.tools.guimixin import GuiMixin
from gui.tools.guimaker import *


class ShellGui(GuiMixin, GuiMakerWindowMenu):
    def start(self):
        self.setMenuBar()
        self.setToolBar()
        self.master.title("Shell Tools Listbox")
        self.master.iconname("Shell Tools")

    def handleList(self, event):
        label = self.listbox.get(ACTIVE)
        self.runCommand(label)

    def makeWidgets(self):
        sbar = Scrollbar(self)
        list_ = Listbox(self, bg='white')
        sbar.config(command=list_.yview)
        list_.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list_.pack(side=LEFT, expand=YES, fill=BOTH)
        for (label, action) in self.fetchCommands():
            list_.insert(END, label)
        list_.bind('<Double-1>', self.handleList)
        self.listbox = list_

    def forToolBar(self, label):
        return True

    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label, action, dict(side=LEFT)))
        self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
            ('File', 0, [('Quit', -1, self.quit)]),
            ('Tools', 0, toolEntries)]
        for (label, action) in self.fetchCommands():
            toolEntries.append((label, -1, action))


class ListMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu

    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd:
                action()


class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()

    def runCommand(self, cmd):
        self.myMenu[cmd]()
