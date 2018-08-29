import mypkg.mymod as mymod

mymod.test('/etc/passwd')
print(mymod.countLines('/etc/apt/sources.list'), 
      mymod.countChars('/etc/hosts'), sep='\n')
