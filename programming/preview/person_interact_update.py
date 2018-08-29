from person import Person
import shelve


fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('persondb')

while True:
    key = input('key> ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        current_value = getattr(record, field)
        update_value = input('\t[%s]=%s\n\t\tnew?=>' % (field,
                                                        current_value))
        if update_value:
            setattr(record, field, eval(update_value))
    db[key] = record
db.close()
