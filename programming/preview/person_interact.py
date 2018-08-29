import shelve


fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('persondb')

while True:
    key = input('key> ')

    if not key:
        break
    try:
        record = db[key]
    except Exception as e:
        print('No such key:', key, ':', e)
    else:
        for field in fieldnames:
            print(field, '=>', getattr(record, field))
