'''
Test = decorator(Test) [cls = Test] -> returns Wrapper
Test(1, 2) -> Wrapper(1, 2) [self.wrapped = Test(*(1, 2))]
Therefore, x is instance of Wrapper and Wrapper intercepts calls of
undefined attributes with help of __getattr__(self, attr)
'''


def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, attr):
            return getattr(self.wrapped, attr)

    return Wrapper


@decorator
class Test:
    def __init__(self, x, y):
        self.name = 'Uknown person'


x = Test(1, 2)
print(x.name)
