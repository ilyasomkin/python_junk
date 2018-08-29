import os, sys, glob


dirname = '/usr/lib/python3.7' if len(sys.argv) == 1 else sys.argv[1]
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for file in allpy:
    filesize = os.path.getsize(file)
    allsizes.append((filesize, file))

for (size, file) in sorted(allsizes, reverse=True):
    print(file, '=>', size, 'bytes')
