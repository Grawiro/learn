class CheckAttribute:
    def __init__(self, var=1):
        self._var_1 = var
        self._var_2 = var
        self._var_3 = var

    def getvar(self):
        print('get', end='->')
        return self._var_1

    def setvar(self, var):
        print('set->', var, sep='')
        self._var_1 = var

    # noinspection SpellCheckingInspection
    def delvar(self):
        print('del->', self._var_1, sep='')
        del self._var_1

    # this is properties
    var_1 = property(getvar, setvar, delvar, 'documentation for variable')

    # the same as above,  this is a decorator
    @property  # var_2.getter
    def var_2(self):
        print('get', end='->')
        return self._var_2

    @var_2.setter
    def var_2(self, var):
        print('set->', var, sep='')
        self._var_2 = var

    @var_2.deleter
    def var_2(self):
        print('del->', self._var_2, sep='')
        del self._var_2

    # noinspection PyProtectedMember
    # this class can be outside class
    class Descriptor_var_3:
        """this is a Descriptor/var 3 documentation"""
        def __init__(self):
            # can create local variable here
            print('init Descriptor_var_3')

        def __get__(self, instance, owner):
            print('get', end='->')
            return instance._var_3

        def __set__(self, instance, value):
            print('set->', value, sep='')
            instance._var_3 = value

        def __delete__(self, instance):
            print('del->', instance._var_3, sep='')
            del instance._var_3

    var_3 = Descriptor_var_3()


print('var 1:')
obj = CheckAttribute()
print(CheckAttribute.var_1.__doc__)
print(obj.var_1)
obj.var_1 = 32
print(obj.var_1)
some_var = obj.var_1
print(some_var)
del obj.var_1
print()

print('var 2:')
print(obj.var_2)
obj.var_2 = 32
print(obj.var_2)
del obj.var_2
print()

print('var 3:')
print(CheckAttribute.Descriptor_var_3.__doc__)
print(obj.var_3)
obj.var_3 = 32
print(obj.var_3)
del obj.var_3
print()


class CheckAttributes:
    def __init__(self, var=1):
        self._var_1 = var
        self.var_2 = var

    # take only unknown attributes like var_1
    def __getattr__(self, item):
        if item == 'var_1':
            print('get->', end='')
            return self._var_1
        else:
            raise AttributeError(item)

    # to take all attributes like var_1/var_2
    def __getattribute__(self, item):
        if item == 'var_3':
            print('get->', end='')
            return 3
        return object.__getattribute__(self, item)

    # set all attributes
    def __setattr__(self, key, value):
        if key == 'var_1':
            print('set->', value, sep='')
            key = '_var_1'
        self.__dict__[key] = value

    # delete all attributes
    def __delattr__(self, item):
        if item == 'var_1':
            print('del->', self._var_1, sep='')
            item = '_var_1'
        del self.__dict__[item]


print('var 1:')
obj = CheckAttributes()
print(obj.var_1)
obj.var_1 = 3
del obj.var_1

print(obj.var_2)
print(obj.var_3)

# create variable
obj.var_4 = 4
print(obj.var_4, '\n')
