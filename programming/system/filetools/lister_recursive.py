import os, sys


def lister(curdir):
    print('[' + curdir + ']')
    for file in os.listdir(curdir):
        path = os.path.join(curdir, file)
        if not os.path.isdir(path):
            print('...' + path)
        else:
            lister(path)


if __name__ == '__main__':
    lister(sys.argv[1])
