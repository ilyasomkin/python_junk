def oops():
    raise IndexError('Artificial IndexError raise')


def oop2():
    try:
        oops()
    except IndexError as e:
        print('Index Error caught!', e)
    else:
        print('No error caught')


if __name__ == '__main__':
    oop2()
