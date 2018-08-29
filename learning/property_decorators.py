class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('delete...')
        del self._name


if __name__ == '__main__':
    bob = Person('John Smith')
    print(bob.name)
    bob.name = 'Eric List'
    print(bob.name)
    del bob.name
