from time_decorator_meth import tracer
from types import FunctionType


def decorateAll(decorator):
    class Meta(type):
        def __new__(meta, classname, supers, classdict):
            for (attr, attrvalue) in classdict.items():
                if type(attrvalue) is FunctionType:
                    classdict[attr] = decorator(attrvalue)
            return super().__new__(meta, classname, supers, classdict)

    return Meta


class Person(metaclass=decorateAll(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Edwards', 15000)
print(bob.name)
bob.giveRaise(.10)
print(bob.pay)
print(bob.lastName())
