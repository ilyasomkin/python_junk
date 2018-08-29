import os, sys
l = ['123', '123', '245']
with open('myfile.txt', 'w') as file:
    try:
        file.write('Hello file world!\n')
        file.write('\n'.join(l))
    except:
        sys.exit('Bad file writing')
    finally:
        file.close()

with open('myfile.txt') as file:
    try:
        print(file.read())
    except:
        sys.exit('Bad file reading')
    finally:
        file.close()