class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    x = General()
    raise x


def raiser1():
    y = Specific1()
    raise y


def raiser2():
    z = Specific2()
    raise z


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        import sys
        print('caught:', sys.exc_info()[0])
