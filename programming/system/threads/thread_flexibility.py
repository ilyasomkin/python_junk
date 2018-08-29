import _thread, threading


class Power:
    def __init__(self, i):
        self.i = i

    def action(self):
        print(self.i ** 32)


def action(i):
    def power():
        print(i ** 32)
    return power


obj = Power(2)
threading.Thread(target=obj.action).start()

threading.Thread(target=(lambda: action(2))).start()
_thread.start_new_thread(obj.action, ())
_thread.start_new_thread(action(2), ())
