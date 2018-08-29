r'''
def adder(*pargs):
    first, *rest = pargs
    return first if not rest else first + adder(*rest)

print(adder(2, 3, 4, 5))
print(adder('2', '3'))
print(adder([1, 2, 3], [4, 5, 6]))
print(adder(2.5, 3.4))


def adder4(**kargs):
    args = list(kargs.values())
    first = args[0]
    for arg in args[1:]:
        first += arg
    return first


print(adder4(a=[2,3],b=[4,5],c=[6,7]))


D = {'a': 1, 'b': 2}


def copyDict(dict):
    new_dict = dict.copy()
    return new_dict


D_new = copyDict(D)
D_new['c'] = 3
print(D_new, D)


def addDict(arg1, arg2):
    if type(arg1) == type(arg2) == type({}):
        return dict(list(arg1.items()) + list(arg2.items()))
    elif type(arg1) == type(arg2) == type([]):
        return arg1 + arg2
    return arg1 + arg2


D_concat = addDict([1, 2, 3], [1, 2, 3])
print(D_concat)


def factor(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')


factor(15)
'''


class FirstClass:
    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
print(b)
a.mul(3)
a.display()
print(a)
