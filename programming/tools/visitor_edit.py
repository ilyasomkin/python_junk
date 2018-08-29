from visitor import SearchVisitor
import os
import sys


class EditVisitor(SearchVisitor):
    editor = 'gedit'

    def visitMatch(self, fname, text):
        os.system('%s %s' % (self.editor, fname))


if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited %d files, visited %d' % 
          (visitor.scount, visitor.fcount))
        