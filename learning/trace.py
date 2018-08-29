from math import sqrt
import sys
import time

if sys.platform[:3] == 'win':
    timefunc = time.clock
else:
    timefunc = time.time


def trace(*args):
    pass


def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)

    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)

    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
        elapsed = timefunc() - start
    return (elapsed, ret)


def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best:
            best = time
    return (best, ret)


reps = 10000
repslist = range(reps)


def math_imported():
    for x in repslist:
        res = sqrt(x)
    return res


def math_builtins():
    for x in repslist:
        res = x ** .5
    return res


def math_function():
    for x in repslist:
        res = pow(x, .5)
    return res


print(sys.version)
for tester in (timer, best):
    print('<%s>' % tester.__name__)
    for test in (math_imported, math_builtins, math_function):
        elapsed, result = tester(test)
        print ('-' * 35)
        print ('%s: %.5f => %s' % (test.__name__, elapsed, result))
