class tracer:
    def __init__(self, func):
        print('tracer __init__')
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        print('tracer __call__({0}, {1.__class__.__name__}, \'{2}\')'.format(self.__class__.__name__,
                                                                             *args))
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        print('tracer __get__:')
        print('Wrapper({0}, {1})'.format(self.__class__.__name__,
                                         instance.__class__.__name__))
        return Wrapper(self, instance)


class Wrapper:
    def __init__(self, desc, subj):
        print('Wrapper __init__')
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        print('Wrapper __call__:')
        print('{0}({1}, \'{2}\')'.format(self.desc.__class__.__name__,
                                         self.subj.__class__.__name__,
                                         *args))
        return self.desc(self.subj, *args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


class Person:
    @tracer
    def giveRaise(self, value):
        print(value)


'''
spam(1, 2, 3)
spam('a', 'b', 'c')
spam(a=4, b=5, c=6)
'''
sue = Person()
sue.giveRaise('Test value')
