import os
import sys


findonly = False
rootdir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]

found = removed = 0
for (dir_, subdirs, files) in os.walk(rootdir):
    for file in files:
        if file.endswith('.pyc'):
            fullname = os.path.join(dir_, file)
            print('=>', fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    type_, instance_ = sys.exc_info()[:2]
                    print('*' * 4, 'Failed:', file, type_, instance_)
            found += 1

print('Found', found, 'files, removed', removed)
