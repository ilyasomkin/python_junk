from person import Person, Manager
bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', age=35, job='dev', pay=100000)
tom = Manager('Tom Jones', 25, 50000)

import shelve
db = shelve.open('persondb')

for obj in (bob, sue, tom):
    db[obj.name] = obj

db.close()
