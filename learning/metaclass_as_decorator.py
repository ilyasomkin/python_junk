def Trace(classname, supers, classdict):
    cls = type(classname, supers, classdict)

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, attr):
            print('get:', attr)
            return getattr(self.wrapped, attr)

    return Wrapper


class Person(metaclass=Trace):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


bob = Person('Bob', 15, 50)
print(bob.name)
print(bob.pay())
