'''
In python 3.0 and higher, if necessary, 
define overriding methods in class-wrapper onInstance
to avoid requests to 'object' superclass.
'''


traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('Private attribute: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, '=', value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('Private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)

        return onInstance
    return onDecorator


if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))

    x = Doubler('x is', [1, 2, 3])
    print(x.label)
    x.display()
    x.double()
    x.display()  # ; x.data
