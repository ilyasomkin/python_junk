def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return super().__new__(meta, classname, supers, classdict)


class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = 'ni?'


x = Client1('Test1 is there')
y = Client2()
print(x.spam(), x.eggs(), x.ham('ham test'), sep='\n')
print(y.value)
    