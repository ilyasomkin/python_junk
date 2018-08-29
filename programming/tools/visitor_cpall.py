from visitor import FileVisitor
from system.filetools.cpall import copyfile
import os


class CpallVisitor(FileVisitor):
    def __init__(self, fromDir, toDir, trace=True):
        super(CpallVisitor, self).__init__(trace=trace)
        self.fromDirLen = len(
            fromDir) + 1 if not fromDir.endswith('/') else len(fromDir)
        self.toDir = toDir

    def visitDir(self, dirpath):
        toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        if self.trace:
            print('d', dirpath, '=>', toPath)
        os.mkdir(toPath)
        self.dcount += 1

    def visitFile(self, filepath):
        toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
        if self.trace:
            print('f', filepath, '=>', toPath)
        copyfile(filepath, toPath)
        self.fcount += 1


if __name__ == '__main__':
    import sys
    import time
    fromDir, toDir = sys.argv[1:3]
    trace = len(sys.argv) > 3
    print('Copying...')
    start = time.perf_counter()
    walker = CpallVisitor(fromDir, toDir, trace)
    walker.run(startDir=fromDir)
    print('Copied', walker.fcount, 'files,',
          walker.dcount, 'directories', end=' ')
    print('in %.4f sec' % (time.perf_counter() - start))
