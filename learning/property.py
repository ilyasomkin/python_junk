class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('delete...')
        del self._name

    name = property(getName, setName, delName)


if __name__ == '__main__':
    bob = Person('John Smith')
    print(bob.name)
    bob.name = 'Eric List'
    print(bob.name)
    del bob.name
