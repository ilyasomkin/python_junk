def decorator(func):
    def wrapper(*args):
        func(*args)
    return wrapper


@decorator
def f(x, y):
    print(x, y)


f(8, 9)
