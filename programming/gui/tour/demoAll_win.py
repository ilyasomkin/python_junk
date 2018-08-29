from tkinter import *
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']


def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname) 
        window = Toplevel()
        window.title(module.__name__)
        demo = module.Demo(window)
        demoObjects.append(demo)
    return demoObjects


def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()
        else:
            print('None')


root = Tk()
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()