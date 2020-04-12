###
# class
###

# empty class
class Class_3: pass

# parent class (superclass)
class Class_2:
    _private_variable = 'this is a private variable'
    # this can be use only in a method in class
    # _Class_2__more_private this is a full name
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
    # when create object
    def __init__(self,num_1=1,num_2=3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_list = [self.num_1, self.num_2]

        self.stop_iter = 5
        self.state_iter = 1-1
        self.sms_text=''

    # when delete object
    def __del__(self):
        print('object die')

    # obj + 2
    def __add__(self, tmp):
        self.num_1 += tmp
        return self.num_1

    # 2 + obj, or obj + obj
    # all math operator have r and i version of operations
    def __radd__(self, tmp):
        self.num_2 += tmp
        # better use
        # self.num_2 = tmp + self.num_2
        return self.num_2

    # only in obj += 2
    def __iadd__(self, tmp):
        self.num_1+=int(tmp/2)
        self.num_2+=int(tmp/2)
        return self

    # obj - 2
    def __sub__(self, tmp):
        self.num_1 -= tmp
        return self.num_1

    # obj * 2
    def __mul__(self, tmp):
        pass

    # this use in print and to convert to str
    def __str__(self):
        return 'str: {} {}'.format(self.num_1, self.num_2)

    # this use to convert to str and show in interactive mode
    # and if str not define show in print function
    def __repr__(self):
        return 'repr: {} {}'.format(self.num_1, self.num_2)

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

    # to get attribute who never existed
    def __getattr__(self, attrname):
        if attrname == 'num_pi':
            return 3.14
        else:
            return self.__dict__[attrname]
            # can raise the error if this attribute is not in if above
            # raise AttributeError 

    # to set another method to set all attribute 
    def __setattr__(self, attrname, value):
        if attrname == 'sms':
            self.sms_text = value
        else:
            self.__dict__[attrname] = value

    # call object like function, can do everything
    def __call__(self, *args, **kwargs):
        print('call obj() with arguments: ', args, kwargs)

    # operation obj>2/ obj<2/ obj==2/ obj!=2 /return True or False
    def __gt__(self, tmp):
        return self.num_1 > tmp

    def __lt__(self, tmp):
        return self.num_1 < tmp

    def __eq__(self, tmp):
        return self.num_1 == tmp

    def __ne__(self, tmp):
        return self.num_1 != tmp

    # return True or False
    def __bool__(self):
        return bool(self.num_1)

    # return len of object
    def __len__(self):
        return len(self.num_list)

    # method to property
    def getSMS(self):
        return self.sms_text
    
    # property have (get,set,del,doc) if none are present, insert None
    # if call sms run getSMS, if sms='hello' run for example setSMS or __setattr__
    sms = property(getSMS, __setattr__, None, 'documentation')
    
    # this is a method can be use with object and class
    def bound(self):
        return self.num_1+self.num_2

    # this is a function, which has no self argument
    # this is a function decorator, look down to static_method
    @staticmethod
    def static_method():
        return 10

    # this is a method, with class name argument, this is some like self
    # dont give it yourself
    @classmethod
    def class_method(class_name):
        return class_name.__name__

    # dont take class or object as argument
    # static_method = staticmethod(static_method)
    # takes class as argument
    # class_method = classmethod(class_method)

number = Number()
# str/repr
print(number)
print(repr(number))
print()

# add/sub
print(number - 1)
print(number + 2)
print(2 + number)
print(number + number)
print(number)
number += 12
print(number)
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
number.num_2 = 3
print(bin(number))
print([0,1,2,3,4,5][number])
print()

# contains
print(2 in number)
print()

# getattr/setattr
print(number.num_pi)
number.temp = 3
print(number.temp)
print()

# call
number('this', 932, a='bob', b=99)
print()

# gt/lt/eq/ne/bool/len
print(number>2)
print(number<2)
print(number==2)
print(number!=2)
print(bool(number))
print(len(number))
print()

# use method and function
method = number.bound
print(method())
# this is a function not method
print(Number.bound(number))
# this function dont take self argument
print(Number.static_method())
print(number.static_method())
# only class can use this
print(Number.class_method())
print()

# create object, they die when print function end
print(Number(1,2))
# show id class and object
print(id(Number), id(number))
print()

# this work but __setattr__/__getattr__ must be undefined
number.sms = 'this is a good text'
print(number.sms)
print()

# show all attribute and function
from list_tree import ListTree
class Test_list_tree(ListTree, Number):pass
test = Test_list_tree()
print(test)
print()

# create a object factory 
def factory_class_function(class_name, *args, **kwargs):
    return class_name(*args, **kwargs)

factory_obj_1 = factory_class_function(Number, num_2=2, num_1=3)
print(factory_obj_1)
factory_obj_2 = factory_class_function(Class_1, 'John')
print(factory_obj_2)
print()

print(isinstance(factory_obj_1, object), isinstance(factory_obj_1, Number))
print()

class Slots_class():
    # can use only this variable in class
    # ['a', 'b'] -the same 
    # if use '__dict__' in [] can normal add variables
    # slots is faster than dict
    __slots__ = ['a', 'b']

some_slots_object = Slots_class()
some_slots_object.a=3
print(some_slots_object.a)
# use setattr/getattr to set and get attribute of class
# work with slots and dict
setattr(some_slots_object, 'a', 2)
print(getattr(some_slots_object, 'a'))
print()

# create my new unction decorator can be use in global function
# and may have only init and call method
class my_function_decorator:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call {} to {}'.format(self.calls, self.func.__name__))
        self.func(*args)

@my_function_decorator
def some_function(a,b,c):
    print(a, b, c)

# realy call to my_function_decorator()/my_function_decorator.__call__
some_function(1,2,3)
some_function('a','b','c')
some_function([1,2,3],(1,2,3),{'a':1,'b':2})
print()

# this is a class decorator work similar to function decorator
def count(aClass):
    aClass.numInstances = 0
    return aClass

@count
class Spam:
    pass

# this is a meta class
class Meta(type):
    def __new__(meta, classname, supers, classdict):
        pass

class C(metaclass=Meta):
    pass