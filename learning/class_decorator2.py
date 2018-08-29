def Tracer(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, attr):
            print('Trace:', attr)
            self.fetches += 1
            return getattr(self.wrapped, attr)

    return Wrapper


@Tracer
class Spam:
    def display(self):
        print('Spam')


@Tracer
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


food = Spam()
food.display()
print([food.fetches])
bob = Person('Bob', 42, 12)
print(bob.name)
print(bob.pay())
