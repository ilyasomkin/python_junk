import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:
        os.execlp('python3.7', 'python3.7', 'child.py', str(parm))
        assert False, 'Error starting program'
    else:
        print('Child is', pid)
        if input() == 'q':
            break
