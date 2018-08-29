class Stepper:
    def __getitem__(self, i):
        return self.data[i]


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class Iters:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, i):
        print('get[%s]: ' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end='')
        self.index = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.index == len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
    print()
    iters = Iters([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    for i in iters:
        print(i, end=' | ')
    print()
    print(iters[::2])
    print(3 in iters)
    print([i ** 2 for i in iters])
    print(list(map(bin, iters)))
    '''
    test = Stepper()
    test.data = 'test string'

    for x in Squares(1, 5):
        print(x, end=' ')
    for i in test:
        print(i, end='')
    print(list(map(str.upper, test)))
    '''
