class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return '<Employee: name = {0}, salary = {1}>'.format(self.name,
                                                             self.salary)


class Chef(Employee):
    def __init__(self, name):
        # Employee.__init__(self, name, salary=50000)
        super(Chef, self).__init__(name, salary=50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    def __init__(self, name):
        # Employee.__init__(self, name, salary=40000)
        super(Server, self).__init__(name, salary=40000)

    def work(self):
        print(self.name, 'interfaces with customer')


class PizzaRobot(Chef):
    def __init__(self, name):
        # Chef.__init__(self, name)
        super(PizzaRobot, self).__init__(name)

    def work(self):
        print(self.name, 'makes pizza')


if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(.20)
    print(bob)
    print()

    for cls in Employee, Chef, Server, PizzaRobot:
        obj = cls(cls.__name__)
        obj.work()
