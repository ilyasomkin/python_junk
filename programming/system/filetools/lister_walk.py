import os, sys


def lister(root):
    for dir, subdir, files in os.walk(root):
        print('[' + dir + ']')
        for file in files:
            path = os.path.join(root, file)
            print('...' + path)


if __name__ == '__main__':
    lister(sys.argv[1])
