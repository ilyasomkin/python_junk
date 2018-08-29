def MetaFunc(classname, supers, classdict):
    print('In MetaFunc:', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)


class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print('In Meta.__new__:', classname, supers, classdict, sep='\n...')
        return super().__new__(meta, classname, supers, classdict)

    def __init__(cls, classname, supers, classdict):
        print('In Meta.__init__:', classname, supers, classdict, sep='\n')
        print('...init class object:', list(cls.__dict__.keys()))


class Eggs:
    pass


print('making class')


class Spam(Eggs, metaclass=Meta):  # metaclass=MetaFunc
    data = 1

    def meth(self, arg):
        pass


print('making instance')
x = Spam()
print('data:', x.data)
