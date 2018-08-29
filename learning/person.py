class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for attr in sorted(self.__dict__):
            attrs.append('{0}={1}'.format(attr, getattr(self, attr)))
        return ', '.join(attrs)

    def __str__(self):
        return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    def __init__(self, name, pay):
        # Person.__init__(self, name, 'mgr', pay)
        super(Manager, self).__init__(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        # Person.giveRaise(self, percent + bonus)
        super(Manager, self).giveRaise(percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Hall', 150000)
    print(sue)
    print(bob)
    print(bob.lastName(), sue.lastName(), sep='\n')
    sue.giveRaise(.10)
    tom.giveRaise(.10)
    print(sue, tom, sep='\n')
    '''
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    '''
