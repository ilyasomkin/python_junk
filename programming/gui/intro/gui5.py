from tkinter import *


class HelloButton(Button):
    def __init__(self, master=None, **config):
        super(HelloButton, self).__init__(master, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodbye world...')
        self.quit()


if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()
