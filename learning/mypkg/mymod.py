def countLines(name):
    global file
    file = open(name)
    return('{0}: {1} line(s)'.format(name,
                                     len(file.readlines())))


def countChars(name):
    file.seek(0)
    return('{0}: {1} characters'.format(name,
                                        len(file.read())))


def test(name):
    print('{0}\n{1}'.format(countLines(name),
                            countChars(name)))


if __name__ == '__main__':
    test('/etc/passwd')
    test('/etc/hosts')
