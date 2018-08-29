import os
import sys


class FileVisitor:
    def __init__(self, context=None, trace=2):
        self.fcount = 0
        self.dcount = 0
        self.context = context
        self.trace = trace

    def run(self, startDir=os.curdir, reset=True):
        if reset:
            self.reset()
        for (dir_, subdirs, files) in os.walk(startDir):
            self.visitDir(dir_)
            for fname in files:
                fpath = os.path.join(dir_, fname)
                self.visitFile(fpath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitDir(self, dirpath):
        self.dcount += 1
        if self.trace > 0:
            print(dirpath, '...')

    def visitFile(self, filepath):
        self.fcount += 1
        if self.trace > 1:
            print(self.fcount, '=>', filepath)


class SearchVisitor(FileVisitor):
    # list of files' extensions to skip
    skipexts = []
    # list of files' extensions to find <searchkey> pattern in
    exts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']

    def __init__(self, searchkey, trace=2):
        super(SearchVisitor, self).__init__(searchkey, trace)
        self.scount = 0

    def reset(self):
        self.scount = 0

    def candidate(self, fname):
        ext = os.path.splitext(fname)[1]
        if self.exts:
            return ext in self.exts
        else:
            return ext not in self.skipexts

    def visitFile(self, fname):
        super(SearchVisitor, self).visitFile(fname)
        if not self.candidate(fname):
            if self.trace > 0:
                print('Skipping', fname)
        else:
            text = open(fname, 'rb').read()
            if self.context.encode() in text:
                self.visitMatch(fname, text)
                self.scount += 1

    def visitMatch(self, fname, text):
        print('%s has %s' % (fname, self.context))


if __name__ == '__main__':
    dolist = 1
    dosearch = 2
    donext = 4

    def selftest(testmask):
        if testmask & dolist:
            visitor = FileVisitor(trace=2)
            visitor.run(sys.argv[2])
            print('Visited %d files and %d dirs' %
                  (visitor.fcount, visitor.dcount))

        if testmask & dosearch:
            visitor = SearchVisitor(sys.argv[3], trace=0)
            visitor.run(sys.argv[2])
            print('Found <%s> in %d files, visited %d' %
                  (sys.argv[3], visitor.scount, visitor.fcount))

    selftest(int(sys.argv[1]))
