from second_ex import MyList

class MyListSub(MyList):
    calls = 0

    def __init__(self, data):
        print('In MyListSub inheritor __init__')
        self.adds = 0
        MyList.__init__(self, data)

    def __add__(self, value):
        print('In MyListSub inheritor __add__')
        MyListSub.calls += 1
        self.adds += 1
        return MyList.__add__(self, value)

    def displayCounters(self):
        return self.calls, self.adds


obj = MyListSub('eggs')
obj2 = MyListSub('odd')
print(obj + ['spam'])
print(obj + ['odd'])
print(obj2 + ['spam'])
obj.append('poem')
print(obj)
print(obj.displayCounters())
