###
# class
###

# empty class
class Class_3: pass

# parent class (superclass)
class Class_2:
    _private_variable = 'this is a private variable'
    # this can be use only in a method in class
    __more_private = 'this one is much more private'
    
    def ger_private(self):
        return self.__more_private

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

    # may use in init to create a local var instantly
    to_all_object = 'this is a common variable'

    def get_to_all_object(self):
        # this object have two state local and global
        return self.to_all_object, Class_1.to_all_object

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

# create list of object 
company = [object_1, object_2]
for emp in company:
    print(emp.getname())

# use + operator
object_3 = object_1 + 'ek'
print(object_3)

print()
# this is a global class variable
print(object_1.to_all_object)
# change global class variable
Class_1.to_all_object = 'something'
print(object_2.to_all_object)
# now this is a local variable
object_1.to_all_object = 'nothing'
print(object_1.to_all_object)
print(object_2.to_all_object)
print(object_1.get_to_all_object())

# use private variables
print(object_1._private_variable)
print(object_1.ger_private())
# this work but give a warning
#print(object_1._Class_2__more_private)
print()

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
print(dir(object_1))
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
print()

# this is must to create abstract class
from abc import ABCMeta, abstractmethod

class Abstract_class(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    # this is a abstract method, must be create to create a object
    #  of subclass
    @abstractmethod
    def action(self):
        pass

class Sub_abstract_class(Abstract_class):
    def action(self):pass

object_abstract_class = Sub_abstract_class()

class Number:
    def __init__(self,num_1=1,num_2=3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_list = [self.num_1, self.num_2]

        self.stop_iter = 5
        self.state_iter = 1-1

    # +
    def __add__(self, tmp):
        self.num_1 += tmp
        return self.num_1
    # -
    def __sub__(self, tmp):
        self.num_1 -= tmp
        return self.num_1

    def __str__(self):
        return '{} {}'.format(self.num_1, self.num_2)

    # to use [0]/[1]/[-1]/[:]/[2:10:3]
    # to work on list/tuple/map/for/in...
    def __getitem__(self, index):
        return self.num_list[index]

    # to set value obj[0] = value
    def __setitem__(self, index, value):
        self.num_list[index] = value

    # convert to hex/oct/bin or int but only in [obj]
    def __index__(self):
        return self.num_2

    # if iter and next are defined getitem dont work
    # use in list/tupel/for/map/in...
    # iter only start iteration next return next element
    def __iter__(self):
        # return self to have one iteration at the time or new class to have 
        # many iteration at the time
        return Number()
    
    def __next__(self):
        if self.state_iter == self.stop_iter:
            self.state_iter = 0
            raise StopIteration
        self.state_iter += 1
        return self.state_iter

    # prefer to use in 'in' opertaion
    def __contains__(self, tmp):
        return tmp in self.num_list


number = Number()
# str
print(number)
print()

# add/sub
print(number - 1)
print(number + 2)
print()

# getitem/setitem
print(number[0])
number[0]=4
print(number[0])

# getitem/iter/next
for i in number:
    for j in number:
        print(i+j,end='->')
print('\n'+str(list(number)), tuple(number))
print([x for x in number])
print(list(map(lambda x: x+1, number)))
print()

# index
print(bin(number))
print([0,1,2,3,4,5][number])
print()

# contains
print(2 in number)






















































# raise some error
# assert False, 'działanie musi zostać zdefiniowane!
# raise NotImplementedError
#  
#__setattr__ - ustawianie prywatnosci
# __slots__
# __repr__ -sposob wyswietlania w trybie interaktywnym????

# __len__/__bool__/__lt__