class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value

    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('Invalid age value')
            self.age = value

    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('Invalid account number')
            self.acct = value

    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError('Can\'t set \'remain\' attribute')

    remain = Remain()


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
