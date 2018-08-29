from tkinter import *
from tkinter.dialog import Dialog


class OldDialogFrame(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super(OldDialogFrame, self).__init__(master, cnf={}, **kw)
        self.pack()
        Button(self, text='Pop1', command=self.dialog1).pack()
        Button(self, text='Pop2', command=self.dialog2).pack()

    def dialog1(self):
        answer = Dialog(self,
                        title='PopUp Fun',
                        text='An example of popup-dialog box (old)',
                        bitmap='questhead',
                        default=0, strings=('Yes', 'No', 'Cancel'))
        if answer.num == 0:
            self.dialog2()

    def dialog2(self):
        Dialog(self, title='HAL-9000',
               text='I am afraid I cannot let you do that, Dave...',
               bitmap='hourglass',
               default=0, strings=('spam', 'SPAM'))


if __name__ == '__main__':
    OldDialogFrame().mainloop()
