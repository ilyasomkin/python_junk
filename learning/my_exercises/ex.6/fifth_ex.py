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


class SetExtended(Set):
    def intersect(self, *args):
        # or def intersect(*args):
        # ...
        # for x in args[0]:
        # for other in args[1:]: ...
        res = []
        for x in self:
            for other in args:
                if x not in other:
                    break
            else:
                res.append(x)
        return Set(res)

    def union(*args):
        res = []
        for arg in args:
            for entry in arg:
                if entry not in res:
                    res.append(entry)
        return Set(res)


if __name__ == '__main__':
    '''
    set1 = Set([1, 2, 3, 4, 5, 6, 7])
    set2 = Set([4, 5, 6, 7, 8, 9, 10])
    set3 = Set('test str')
    str1 = 'test'
    print(set3 & str1)
    print(set3[::])
    print(set1 & set2)
    print(set1 | set2)
    '''
    multi1 = SetExtended([1, 2, 3, 4, 8, 9, 10])
    multi2 = SetExtended([4, 5, 6, 7, 8, 9, 10])
    multi3 = SetExtended([8, 9, 10])
    print(multi1.intersect(multi2, multi3))
    print(multi1.union(multi2, multi3))
