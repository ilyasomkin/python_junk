import os
import fnmatch


def find(pattern, startdir=os.curdir):
    for (dir_, subdirs, files) in os.walk(startdir):
        for name in subdirs + files:
            if fnmatch.fnmatch(name, pattern):
                fullpath = os.path.join(dir_, name)
                yield fullpath


def findlist(pattern, startdir=os.curdir, do_sort=False):
    matches = list(find(pattern, startdir))
    if do_sort:
        matches.sort()
    return matches


if __name__ == '__main__':
    import sys
    namepattern, startdir = sys.argv[1], sys.argv[2]
    for name in find(namepattern, startdir):
        print(name)
