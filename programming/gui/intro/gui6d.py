from tkinter import *
from gui6 import Hello


class HelloExtender(Hello):
    def create_widgets(self):
        super(HelloExtender, self).create_widgets()
        Button(master=self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('hello', self.data)


if __name__ == '__main__':
    HelloExtender().mainloop()
