import os, sys, pprint


trace = False
if sys.platform.startswith('win'):
    # path to Python (Windows)
    # dirname =
    pass
else:
    dirname = '/usr/lib/python3.7'

allsizes = []
for (curdir, subcurdirs, files) in os.walk(dirname):
    if trace:
        print(curdir)
    for file in files:
        if file.endswith('.py'):
            if trace:
                print('...', file)
            fullname = os.path.join(curdir, file)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

for (size, file) in sorted(allsizes, reverse=True):
    print(file, '=>', size, 'bytes')
