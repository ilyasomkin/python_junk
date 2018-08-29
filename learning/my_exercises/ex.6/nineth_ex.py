class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line('that\'s one ex-bird!')
        self.clerk.line('no it isn\'t...')
        self.parrot.line(None)


class Base:
    def line(self, text):
        print('{0}: {1}'.format(self.name,
                                text))


class Customer(Base):
    name = 'customer'


class Clerk(Base):
    name = 'clerk'


class Parrot(Base):
    name = 'parrot'


Scene().action()
