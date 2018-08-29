import os
import sys


maxfilesize = 1000000
bulksize = 1024 * 500


def copyfile(pathFrom, pathTo, maxfilesize=maxfilesize):
    if os.path.getsize(pathFrom) <= maxfilesize:
        bytesFrom = open(pathFrom, 'rb').read()
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')
        fileTo = open(pathTo, 'wb')
        while True:
            bytesFrom = fileFrom.read(bulksize)
            if not bytesFrom:
                break
            fileTo.write(bytesFrom)


def copytree(dirFrom, dirTo, verbose=False):
    fcount = dcount = 0
    for file in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom, file)
        pathTo = os.path.join(dirTo, file)
        if not os.path.isdir(pathFrom):
            try:
                if verbose:
                    print('Copying', pathFrom, 'to', pathTo)
                copyfile(pathFrom, pathTo)
                fcount += 1
            except:
                print('Error copying', pathFrom, 'to', pathTo)
                print(sys.exc_info()[:1])
        else:
            if verbose:
                print('Copying dir', pathFrom, 'to', pathTo)
            try:
                os.mkdir(pathTo)
                below = copytree(pathFrom, pathTo)
                fcount += below[0]
                dcount += below[1]
                dcount += 1
            except:
                print('Error creating', pathTo)
                print(sys.exc_info()[:1])

    return fcount, dcount


def getargs():
    try:
        dirFrom, dirTo = sys.argv[1:]
    except:
        print('Usage error:', sys.argv[0], '<copy from dir> <to dir>')
    else:
        if not os.path.isdir(dirFrom):
            print('Error:', dirFrom, 'is not a directory')
        elif not os.path.isdir(dirTo):
            os.mkdir(dirTo)
            print('Note:', dirTo, 'was created')
            return dirFrom, dirTo
        else:
            print('Warning:', dirTo, 'already exists')
            if hasattr(os.path, 'samefile'):
                same = os.path.samefile(dirFrom, dirTo)
            else:
                same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
            if same:
                print('Error:', dirFrom, 'same as', dirTo)
            else:
                return dirFrom, dirTo


if __name__ == '__main__':
    import time
    dirstuple = getargs()
    if dirstuple:
        print('Copying...')
        start = time.perf_counter()
        fcount, dcount = copytree(*dirstuple, verbose=True)
        print('Copied', fcount, 'files,', dcount, 'directories', end=' ')
        print('in %.4f sec' % (time.perf_counter() - start))
