from types import FunctionType


def extra(self, val):
    self.val_2 = val
    print(self.val_2)


# this is metaclass, add method to another class, must inherited after type
# noinspection PyMethodParameters,SpellCheckingInspection
class Extra(type):
    def __init__(meta, classname, supers, classdict):
        test = True
        if test:
            # in init this method to add new method to class
            meta.extra = extra
            # in new this method to add new method to class
            # classdict['extra'] = extra


# decorator work the same as metaclass in this situation
# must add @Extra_v2 before class
def Extra_v2(aClass):
    aClass.extra = extra
    return aClass


class Class_1(metaclass=Extra):
    def __init__(self):
        self.val_1 = 1


# metaclass can be use many times in many class
class Class_2(metaclass=Extra):
    pass


obj = Class_1()
print(obj.val_1)
obj.extra(2)
print(obj.val_2)
obj = Class_2()
obj.extra(3)
print()


# call method can be change to new method, both do the same
# but call method can use only in metaclass metaclass, here only in SuperMeta
# noinspection PyMethodParameters,SpellCheckingInspection
class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)


# meta class may have __new__/__init__ method
# noinspection PyMethodParameters,SpellCheckingInspection
class MetaOne(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaOne.init:', classname, supers, classdict, sep='\n...')
        print('...class ocject:', list(Class.__dict__.keys()))


# this is the same as above but in the function
# noinspection SpellCheckingInspection
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)


print('Create class')


class Spam(object, metaclass=MetaOne):
    data = 1


print('create object')
X = Spam()
print('data:', X.data)


# this two is the same like SuperMeta nad MetaOne
# but in this class cant use method new and init so must
# have new name like New and Init
# noinspection SpellCheckingInspection
class SuperMeta_1:
    def __call__(self, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class


# in class must use metaclass=SubMeta() with ()
# noinspection SpellCheckingInspection,PyMethodMayBeStatic
class SubMeta(SuperMeta_1):
    def __New__(self, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMeta.init:', classname, supers, classdict, sep='\n...')
        print('...class object:', list(Class.__dict__.keys()))


# this „metaclass” can trace the class attributes
# noinspection SpellCheckingInspection
def Tracer(classname, supers, classdict):
    # must self create a class instance
    aClass = type(classname, supers, classdict)

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, attr_name):
            print('call to:', attr_name)
            return getattr(self.wrapped, attr_name)
    return Wrapper


class Spam(metaclass=Tracer):
    data = 1


print()
X = Spam()
print('data:', X.data)


def tracer(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('calls %s %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


# give a decorator to use
def decorateAll(decorator):
    # noinspection PyMethodParameters,SpellCheckingInspection
    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                # check the attributes to find all method
                if type(attrval) is FunctionType:
                    # decorate method to tracer for example, its the same as @tracer
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate


# noinspection PyMethodMayBeStatic
class Spam(metaclass=decorateAll(tracer)):
    def some_method(self):
        print('something')


print()
X = Spam()
X.some_method()
