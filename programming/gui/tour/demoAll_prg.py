from tkinter import *
from launchmodes import PortableLauncher


demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

for demo in demoModules:
    PortableLauncher(demo, demo + '.py')()


root = Tk()
root.title('Processes')
Label(master=root, text='Multiple program demo: command lines',
      bg='white').pack()
root.mainloop()
