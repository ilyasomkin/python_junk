import time


def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {0} to {1}'.format(calls, func.__name__))
        return func(*args, **kwargs)

    return onCall


def timer(label='', trace=True):
    alltime = 0

    def onDecorator(func):
        def onCall(*args, **kwargs):
            nonlocal alltime
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            alltime += elapsed
            if trace:
                format = '%s %s: elapsed: %.5f, all time: %.5f'
                value = (label, func.__name__, elapsed, alltime)
                print(format % value)
            return result

        return onCall
    return onDecorator


class CallMeasures:
    @timer(label='==>')
    def listcomp(self, N):
        return [x * 2 for x in range(N)]

    @timer(label='-->', trace=True)
    def mapcall(self, N):
        return list(map(lambda x: x * 2, range(N)))


if __name__ == '__main__':
    test = CallMeasures()
    for func in (test.listcomp, test.mapcall):
        func(1000)
        func(100000)
        func(200000)
