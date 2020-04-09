from class_tools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= 1+(percent/100)

    def getPay(self):
        return self.pay

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    # must use the existing code
    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent+bonus)

# this is a second method to connect class composite, use object to call a mathod
# in superclass
class Manager_v2:
    # create a object
    def __init__(self, name, pay):
        self.person = Person(name, 'manager', pay)
    
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)
    
    # use object atribute
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    
    def __str__(self):
        return str(self.person)

# this class group object
class Department:
    def __init__(self, *args):
        self.members = list(args)
    
    def addMember(self, person):
        self.members.append(person)
    
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    
    def showAll(self):
        for person in self.members:
            print(person)
    
if __name__ == "__main__":
    bob = Person('Bob Smith', 'programmer', 10000)
    anna = Person('Anna Smile')
    print (bob.name, bob.job, bob.pay)
    print(anna.name, anna.job, anna.pay)
    bob.giveRaise(22.4)
    print(bob.lastName(), bob.getPay())
    print(bob)

    tom = Manager('Tom Black', 13000)
    tom.giveRaise(15)
    print(tom)

    print()
    development = Department(bob, anna)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    print()

    for key in bob.__dict__:
        print(key, '=>', bob.__dict__[key])
        # the same
        # print(key, '=>', getattr(bob, key))

    # to save object in file 
    import shelve
    database = shelve.open('person_database')
    database.clear()
    for obj in [bob, anna, tom]:
        database[obj.name] = obj
    database.close()