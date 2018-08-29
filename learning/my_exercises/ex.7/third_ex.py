from second_ex import oops
import sys
import traceback


def safe(func, *args):
    try:
        func(*args)
    except:
        traceback.print_exc()
        print('Caught:', sys.exc_info()[:2])


safe(print, 'string literal', 'and another one')
safe(oops)
