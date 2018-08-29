class Adder:
    def __init__(self, data):
        self.data = data

    def __add__(self, value):
        return self.add(self.data, value)

    def add(self, x, y):
        raise NotImplementedError('Not Implemented')


class ListAdder(Adder):
    def add(self, x, y):
        if isinstance(x, list) and isinstance(y, list):
            return x + y
        raise TypeError('Expected <list> as argument type')


class DictAdder(Adder):
    new_dict = {}

    def add(self, x, y):
        if isinstance(x, dict) and isinstance(y, dict):
            for d in (x, y):
                self.new_dict.update(d)
            return self.new_dict
        raise TypeError('Expected <dict> as argument type')


a = ListAdder([1, 2, 3])
b = [4, 5, 6]
d1 = {1: 2, 3: 4}
d2 = {5: 6, 7: 8}
c = DictAdder(d1)
print(a + b)
print(c + d2)
