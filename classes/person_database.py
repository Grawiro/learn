import shelve
from person import Person, Manager

database = shelve.open('person_database')
print(len(database))

barry = database[list(database.keys())[2]]
print(barry)

for i in database:
    print(i, database[i])

barry.name='Barry Thomas'
barry.giveRaise(10)
print(barry)

database[barry.name] = barry

database.close()