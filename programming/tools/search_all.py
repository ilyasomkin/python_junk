import os
import sys


listonly = False
exts = ['.py', '.pyw', '.txt', '.c', '.h']


def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (dir_, subdirs, files) in os.walk(startdir):
        for file in files:
            fpath = os.path.join(dir_, file)
            visitfile(fpath, searchkey)


def visitfile(fpath, searchkey):
    global fcount, vcount
    print(vcount + 1, '=>', fpath)
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in exts:
                print('Skipping', fpath)
            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath, searchkey))
                fcount += 1
    except:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1


if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found <%s> in %d files, visited %d' % (sys.argv[2], fcount, vcount))
