class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid age value')
        self.__age = value

    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('Invalid account number')
        self.__acct = value

    acct = property(getAcct, setAcct)

    def remainGet(self):
        return self.retireage - self.age

    remain = property(remainGet)


if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Davis', 40, '123 highway st.')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')

    sue = CardHolder('8765-1234', 'Sue Johnes', 35, '75 Waydown st.')
    print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
    try:
        sue.age = 200
    except Exception as e:
        print('Bad age for Sue:', e)

    try:
        sue.remain = 5
    except Exception as e:
        print('Can\'t set sue.remain:', e)

    try:
        sue.acct = '1234567'
    except Exception as e:
        print('Bad acct for Sue:', e)
