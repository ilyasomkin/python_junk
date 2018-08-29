'''
In python 3.0 and higher, if necessary, 
define overriding methods in class-wrapper onInstance
to avoid requests to 'object' superclass.
'''


traceMe = False


def trace(*args):
    if traceMe:
        print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass

        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)

            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('Private attribute: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, '=', value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('Private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)

        return onInstance
    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))


def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


if __name__ == '__main__':
    traceMe = True

    @Private('age', 'pay')
    class Person:
        def __init__(self, name, age, pay):
            self.name = name
            self.age = age
            self.pay = pay

    bob = Person('Bob Williams', 45, 15500)
    print(bob.name)

    try:
        print(bob.age)
    except Exception as e:
        print('Exception occurred:', e)

    @Public('name')
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    sue = Person('Sue Jackson', 35)
    print(sue.name)

    try:
        print(sue.age)
    except Exception as e:
        print('Exception occurred:', e)
