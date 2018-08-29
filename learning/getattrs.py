class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):
        print('get:', attr)
        return 3


class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('get:', attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


if __name__ == '__main__':
    x = GetAttr()
    print(x.attr1)
    print(x.attr2)
    print(x.attr3)
    print('-' * 20)
    x = GetAttribute()
    print(x.attr1)
    print(x.attr2)
    print(x.attr3)
