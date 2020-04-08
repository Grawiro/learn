###
# class
###

# empty class
class Class_3: pass

# parent class (superclass)
class Class_2:
    def getname(self):
        print("hello, I don't know your name")
    

# this is a subclass, which inheritances with Class__2 and 3
class Class_1 (Class_2, Class_3):
    # this is a constructor,  self means set yourself as arguments
    def __init__(self, who='no one'):
        # create a variable in the class instance
        self.name = who

    # some get and set functions
    def setname(self, who):
        self.name = who
    
    # this function override function with the same name in Class_2 
    def getname(self):
        return self.name

    # create a new object 
    def __add__(self, tmp):
        return Class_1(self.name + tmp)

    def __str__(self):
        return 'this is a '+ self.name

# create a object (class instance)
object_1 = Class_1('Karol')
print(object_1.getname())
object_1.setname('Kamil')
print(object_1.getname())
# create a local variable olny in this object
object_1.anothername = 'Bob'
print(object_1.anothername)
# use str function
print(object_1)

object_2 = Class_1()
# other method to use class method
Class_1.setname(object_2, 'Tom')
print(Class_1.getname(object_2))

# use + operator
object_3 = object_1 + 'ek'
print(object_3)

# create a variable used in the whole class
Class_3.data = 'some information'
print(Class_3.data)
object_4 = Class_3()
print(object_4.data)
# this information is see in subclass too
print(object_1.data)

# show variables and function in class and object
print(Class_1.__dict__.keys())
print(Class_3.__dict__.keys())
print(object_1.__dict__.keys())

# show class name and superclass
print(object_1.__class__)
print(Class_1.__bases__)

def upperName(self):
    return self.name.upper()
    
# this is a function work on object
print(upperName(object_1))

# now this is a new method, available to all object this class
Class_1.upper_name = upperName
print(object_2.upper_name())

















# company = [object_1, object_2]
# for emp in company:
#     print(emp.getname())


































#__slots__