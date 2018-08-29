import os, sys, pprint


trace = 1
dirname, extname = '/root/Documents', '.py'
if len(sys.argv) > 1:
    dirname = sys.argv[1]
if len(sys.argv) > 2:
    extname = sys.argv[2]
if len(sys.argv) > 3:
    trace = int(sys.argv[3])


def tryprint(*args):
    try:
        print(*args)
    except UnicodeEncodeError:
        print('Encoding error')


visited = set()
allsizes = []
for (curdir, subdirs, files) in os.walk(dirname):
    if trace:
        tryprint(curdir)
    curdir = os.path.normpath(curdir)
    fixcase = os.path.normcase(curdir)
    if fixcase in visited:
        if trace:
            tryprint('Skipping', curdir)
    else:
        visited.add(fixcase)
        for file in files:
            if file.endswith(extname):
                if trace > 1:
                    tryprint('+++', file)
                fullname = os.path.join(curdir, file)
                try:
                    bytesize = os.path.getsize(fullname)
                    linesize = sum(+1 for line in open(fullname, 'rb'))
                except Exception:
                    print('Error', sys.exc_info()[0])
                else:
                    allsizes.append((bytesize, linesize, fullname))

'''
for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('By %s...' % title)
    allsizes.sort(key=lambda x: x[key], reverse=True)
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
'''

print('By size...')
for (size, lines, file) in sorted(allsizes, reverse=True):
    print(file, '=>', size, 'bytes')

print('By lines...')
for (size, lines, file) in sorted(allsizes, key=(lambda x: x[1]), reverse=True):
    print(file, '=>', lines, 'lines')