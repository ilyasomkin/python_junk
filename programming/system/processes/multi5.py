import os
from multiprocessing import Process


def run_program(arg):
    os.execlp('python3.7', 'python3.7', 'child.py', str(arg))


if __name__ == '__main__':
    for i in range(5):
        Process(target=run_program, args=(i,)).start()
    print('parent exit')
