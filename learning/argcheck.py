trace = True


def rangetest(**argchecks):
    def onDecorator(func):
        code = func.__code__
        allargs = code.co_varnames[:code.co_argcount]
        funcname = func.__name__

        def onCall(*pargs, **kargs):
            positionals = list(allargs)
            positionals = positionals[:len(pargs)]

            for (argname, (low, high)) in argchecks.items():
                if argname in kargs:
                    if kargs[argname] < low or kargs[argname] > high:
                        errmsg = '{0} argument \'{1}\' not in {2}..{3}'
                        errmsg = errmsg.format(funcname, argname,
                                               low, high)
                        raise TypeError(errmsg)

                elif argname in positionals:
                    position = positionals.index(argname)
                    if pargs[position] < low or pargs[position] > high:
                        errmsg = '{0} argument \'{1}\' not in {2}..{3}'
                        errmsg = errmsg.format(funcname, argname,
                                               low, high)
                        raise TypeError(errmsg)

                else:
                    if trace:
                        print('Argument \'{0}\' defaulted'.format(argname))

            return func(*pargs, **kargs)
        return onCall
    return onDecorator


@rangetest(age=[0, 120])
def persinfo(name, age):
    print('%s is %s years old' % (name, age))


@rangetest(M=[1, 12], D=[1, 31], Y=[0, 2018])
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))


@rangetest(a=(1, 10), b=(1, 10), c=(1, 10))
def omitargs(a, b=7, c=8):
    print(a, b, c)


class Person:
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    @rangetest(percent=[0.0, 1.0])
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


try:
    persinfo('John Davis', age=45)
    persinfo('Sam Fisher', 121)
except Exception as e:
    print('Exception occurred:', e)

try:
    birthday(3, 26, 1996)
    birthday(4, D=7, Y=2020)
except Exception as e:
    print('Exception occurred:', e)

try:
    omitargs(c=7, a=3)
except Exception as e:
    print('Exception occurred:', e)

try:
    sue = Person('Bob Davis', 'dev', 25000)
    sue.giveRaise(.10)
    print(sue.pay)
    sue.giveRaise(1.10)
except Exception as e:
    print('Exception occurred:', e)
