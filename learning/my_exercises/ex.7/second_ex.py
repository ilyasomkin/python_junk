class MyError(Exception):
    pass


def oops():
    raise MyError('Custom error occured!')
    # raise IndexError('IndexError occured!')


def oop2():
    try:
        oops()
    except (MyError, IndexError) as e:
        print(e, 'Error caught, args:', e.args)
    else:
        print('No error caught')


oop2()
