import sys
from launchmodes import QuietPortableLauncher


numclients = 8


def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()


args = ''.join(sys.argv[1:])
for i in range(numclients):
    start('echo_client.py %s' % args)
