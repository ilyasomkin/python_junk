from visitor import FileVisitor
import os
import sys
import pprint


class BigPy(FileVisitor):
    def __init__(self, trace=0):
        super(BigPy, self).__init__(context=[], trace=trace)

    def visitFile(self, filepath):
        super(BigPy, self).visitFile(filepath)
        if filepath.endswith('.py'):
            print(filepath)
            self.context.append((os.path.getsize(filepath),
                                 filepath))


if __name__ == '__main__':
    walker = BigPy()
    walker.run(sys.argv[1] if len(sys.argv) > 1 else '.')
    print('Visited %d files and %d directories' % (walker.fcount,
                                                   walker.dcount))
    for (size, file) in sorted(walker.context, reverse=True):
        print(size, 'bytes =>', file)
