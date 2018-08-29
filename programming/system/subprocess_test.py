import sys


print('Got this: %s' % input())
data = sys.stdin.readline()[:-1]
print('Meaning of life is', data, int(data) * 2)
