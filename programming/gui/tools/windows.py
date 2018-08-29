import os
import glob
from tkinter import Tk, Toplevel, Frame, YES, BOTH, RIDGE
from tkinter.messagebox import showinfo, askyesno


class _window:
    foundicon = None
    iconpatt = '*.ico'
    iconmine = 'py.ico'

    def configBorders(self, app, kind, iconfile):
        if not iconfile:
            iconfile = self.findIcon()
        title = app
        if kind:
            title += ' - ' + kind
        self.title(title)
        self.iconname(app)
        if iconfile:
            try:
                self.iconbitmap(iconfile)
            except:
                pass
        self.protocol('WM_DELETE_WINDOW', self.quit)

    def findIcon(self):
        if _window.foundicon:
            return _window.foundicon
        iconfile = None
        iconshere = glob.glob(self.iconpatt)
        if iconshere:
            iconfile = iconshere[0]
        else:
            mymod = __import__(__name__)
            path = __name__.split('.')
            for mod in path[1:]:
                mymod = getattr(mymod, mod)
            mydir = os.path.dirname(mymod.__file__)
            myicon = os.path.join(mydir, self.iconmine)
            if os.path.exists(myicon):
                iconfile = myicon
        _window.foundicon = iconfile
        return iconfile


class MainWindow(Tk, _window):
    def __init__(self, app, kind='', iconfile=None):
        super(MainWindow, self).__init__()
        self.findIcon()
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if self.okayToQuit():
            if askyesno(self.__app, 'Verify Quit Program?'):
                self.destroy()
        else:
            showinfo(self.__app, 'Quit not allowed')

    def destroy(self):
        super(MainWindow, self).quit()

    def okayToQuit(self):
        return True


class PopupWindow(Toplevel, _window):
    def __init__(self, app, kind='', iconfile=None):
        super(PopupWindow, self).__init__()
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if askyesno(self.__app, 'Verify Quit Window?'):
            self.destroy()

    def destroy(self):
        super(PopupWindow, self).destroy()


class QuietPopupWindow(PopupWindow):
    def quit(self):
        self.destroy()


class ComponentWindow(Frame):
    def __init__(self, master):
        super(ComponentWindow, self).__init__(master)
        self.pack(expand=YES, fill=BOTH)
        self.config(relief=RIDGE, border=2)

    def quit(self):
        showinfo('Quit', 'Not supported in attachment mode')
