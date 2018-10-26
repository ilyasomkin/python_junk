'''
possible to implement
class Set(list):
    def __init__(self, value=[]):
        list.__init__([])
        self.concat(value)
    ...
to avoid __len__(self), __getitem__(self, key) overriding
'''

class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        result = []
        for x in self.data:
            if x in other:
                result.append(x)
        return Set(result)

    def union(self, other):
        result = self.data[:]
        for x in other:
            if x not in result:
                result.append(x)
        return Set(result)

    def concat(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set: ' + repr(self.data)


if __name__ == '__main__':
    exp1 = Set([1, 2, 3, 4, 5, 6, 6])
    exp2 = Set([3, 4, 5, 5, 6, 7, 8])
    print('Union {0}'.format(exp1.union(exp2)))
    print('Intersection {0}'.format(exp1.intersect(exp2)))
    print(exp1, exp2, sep='\n')
    print(exp1 & exp2)
