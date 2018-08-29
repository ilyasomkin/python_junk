import time


def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                value = (label, self.func.__name__, elapsed, self.alltime)
                print(format % value)
            return result

    return Timer


@timer(label='==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer(label='-->', trace=True)
def mapcall(N):
    return list(map(lambda x: x * 2, range(N)))


for func in (listcomp, mapcall):
    print()
    func(5000)
    func(100000)
