import os, sys


trace = 0

visited = {}
allsizes = []

for srcdir in sys.path:
    for (curdir, subdirs, files) in os.walk(srcdir):
        if trace > 0:
            print(curdir)
        curdir = os.path.normpath(curdir)
        fixcase = os.path.normcase(curdir)
        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True
        for file in files:
            if file.endswith('.py'):
                if trace > 1:
                    print('...', file)
                pypath = os.path.join(curdir, file)
                try:
                    pysize = os.path.getsize(pypath)
                except OSError:
                    print('Skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((pysize, pylines, pypath))

print('By size...')
for (size, lines, file) in sorted(allsizes, reverse=True):
    print(file, '=>', size, 'bytes')

print('By lines...')
for (size, lines, file) in sorted(allsizes, key=(lambda x: x[1]), reverse=True):
    print(file, '=>', lines, 'lines')
