import os, sys


def spawn(program, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()

    # Two-way channels
    parentStdin, childStdout = os.pipe()
    parentStdout, childStdin = os.pipe()
    pid = os.fork()
    if pid:
        # In parent process
        os.close(childStdin)
        os.close(childStdout)
        os.dup2(parentStdin, stdinFd)
        os.dup2(parentStdout, stdoutFd)
    else:
        # In child process
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (program,) + args
        os.execvp(program, args)
        assert False, 'execvp failed'


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python3.7', 'pipes-testchild.py', 'spam')

    print('Hello 1 from parent', mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: "%s"\n' % reply)

    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])
