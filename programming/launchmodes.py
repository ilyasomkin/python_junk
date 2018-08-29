import os, sys


pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python3.7'
pypath = sys.executable


def fixWindowsPath(cmdline):
    splitline = cmdline.lstrip().split(' ')
    fixedpath = os.path.normpath(splitline[0])
    return ' '.join([fixedpath] + splitline[1:])


class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command

    def __call__(self):
        self.announce(self.what)
        self.run(self.where)

    def announce(self, text):
        print(text)

    def run(self, cmdline):
        raise NotImplementedError('Method "run" must be defined')


class System(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' % (pypath, cmdline))


class Popen(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline)


class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork() == 0:
            os.execvp(pypath, [pyfile] + cmdline)
        # else:
        #    os.wait()


class Start(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)


class StartArgs(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start' + cmdline)


class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))


class Top_Level(LaunchMode):
    def run(self, cmdline):
        raise NotImplementedError('Method not implemented yet')


if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass


def selftest():
    print('Parent pid:', os.getppid())
    file_ = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher('running ' + file_, file_)
    launcher()

    input('system mode...')
    System('running ' + file_, file_)()

    if sys.platform[:3] == 'win':
        input('DOS start mode...')
        StartArgs('running ' + file_, file_)()


if __name__ == '__main__':
    selftest()
