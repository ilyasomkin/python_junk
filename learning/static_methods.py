'''
class Methods:
    def imeth(self, x):
        print(self, x)

    def smeth(x):
        print(x)

    def cmeth(cls, x):
        print(cls, x)

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)


obj = Methods()
obj.imeth(2), Methods.imeth(obj, 2.1)
obj.smeth(3), Methods.smeth(4), Methods().smeth(5)
Methods.cmeth(6), obj.cmeth(7)
'''


class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Number of instances:', Spam.numInstances)


class Sub(Spam):
    @staticmethod
    def printNumInstances():
        print('Extra stuff...')
        Spam.printNumInstances()


a, b = Sub(), Sub()
a.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()
