def decorator_1(func): return lambda: 'X' + func()


def decorator_2(func): return lambda: 'Y' + func()


def decorator_3(func): return lambda: 'Z' + func()


@decorator_1
@decorator_2
@decorator_3
def text_func():  # text_func = decorator_1(decorator_2(decorator_3(text_func)))
    return 'abc'


print(text_func())
print()


# noinspection PyShadowingNames
# decorator have be a class or function, with or without
# another logic level
class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("this is {} call of {} result ".format(
            self.calls, self.func.__name__), end='')
        self.func(*args, **kwargs)


# the same as above
def tracer(func):
    calls = 0

    def wrapper_1(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("this is {} call of {} result ".format(
            calls, func.__name__), end='')
        return func(*args, **kwargs)
    return wrapper_1


# this is a function attributes, but work the same
def tracer_v2(func):
    def wrapper_1(*args, **kwargs):
        wrapper_1.calls += 1
        print("this is {} call of {} result ".format(
            wrapper_1.calls, func.__name__), end='')
        return func(*args, **kwargs)
    wrapper_1.calls = 0
    return wrapper_1


@Tracer
def some_add_func_1(a, b, c):
    print(a + b + c)


@tracer
def some_add_func_2(a, b, c):
    print(a + b + c)


some_add_func_1(1, 2, 3)
some_add_func_2(1, 2, 3)
some_add_func_1(10, 12, 11)
some_add_func_2(10, 12, 11)
print()


class tracer_v3:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("this is {} call of {} result ".format(
            self.calls, self.func.__name__), end='')
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return wrapper(self, instance)


class wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)


# this is a decorator with arguments, descriptor work the same
# noinspection PyShadowingNames
def tracer_v4(trace=True):
    class tracer_v5:
        def __init__(self, func):
            self.calls = 0
            self.func = func

        def __call__(self, *args, **kwargs):
            self.calls += 1
            if trace:
                print("this is {} call of {} result ".format(
                    self.calls, self.func.__name__), end='')
            return self.func(*args, **kwargs)

        # this is the same as above __get__ method, but better
        def __get__(self, instance, owner):
            def wrapper_1(*args, **kwargs):
                return self(instance, *args, **kwargs)
            return wrapper_1
    # without this line and def tracer_v4 line, this is the same as
    # description above
    return tracer_v5


class Some_class:
    def __init__(self):
        self.var = 1

    # in method class can use only function [def] decorator
    # like tracer and tracer_v2, or descriptor with __get__
    # method like tracer_v3, or tracer_v4
    @tracer_v3
    def show_var(self):
        print(self.var)


class Some_class_2:
    def __init__(self):
        self.var = 1

    # this one take a one arguments
    @tracer_v4(False)
    def show_var(self):
        print(self.var)


some_object = Some_class()
some_object.show_var()
some_object.show_var()
some_object = Some_class_2()
some_object.show_var()
some_object.show_var()
print()


def singleton_v1(aClass):
    instance = None

    def onCall(*args):
        nonlocal instance
        if instance is None:
            instance = aClass(*args)
        else:
            print('object is exists, return first object')
        return instance
    return onCall


# both is the same
class Singleton_v2:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    # this create only first object
    def __call__(self, *args):
        if self.instance is None:
            self.instance = self.aClass(*args)
        else:
            print('object is exists, return first object')
        return self.instance

    # this create only last object
    # def __call__(self, *args):
    #     self.instance = self.aClass(*args)
    #     return self
    #
    # def __getattr__(self, item):
    #     return getattr(self.instance, item)


@Singleton_v2
class Only_one:
    def __init__(self, var):
        self.var = var

    def show_var(self):
        print(self.var)


only_one_obj_1 = Only_one(99)
only_one_obj_1.show_var()
print(only_one_obj_1.var)
only_one_obj_2 = Only_one(2)
only_one_obj_2.show_var()
print(only_one_obj_1.var)
print()


def range_test_1(*args_checks):
    def onDecorator(func):
        def onCall(*args):
            for (ix, low, high) in args_checks:
                if args[ix] < low or args[ix] > high:
                    print('bad arguments {}'.format(args[ix]))
                    return None
            return func(*args)
        return onCall
    return onDecorator


# this is the same but use annotations in function to work
# and have one level depression less
def range_test_1_v2(func):
    # noinspection SpellCheckingInspection
    def onCall(*pargs):
        argchecks = func.__annotations__
        for ix in range(0, len(argchecks)):
            low, high = list(argchecks.values())[ix]
            if pargs[ix] < low or pargs[ix] > high:
                print('bad arguments {}'.format(pargs[ix]))
                return None
        return func(*pargs)
    return onCall


def range_test_2(**args_checks):
    # noinspection SpellCheckingInspection
    def onDecorator(func):
        # this two return tuple of arguments name in function
        code = func.__code__
        allargs = code.co_varnames[:code.co_argcount]

        # noinspection SpellCheckingInspection
        def onCall(*pargs, **kargs):
            # this one have only positional arguments
            positionals = allargs[:len(pargs)]
            # this one line do the same as this three above
            # positionals = func.__code__.co_varnames[:func.__code__.co_argcount][:len(pargs)]

            for (argname, (low, high)) in args_checks.items():
                if argname in kargs:
                    if kargs[argname] < low or kargs[argname] > high:
                        print('argument "{0}" not in <{1}:{2}>'.format(argname, low, high))
                        return None
                elif argname in positionals:
                    position = positionals.index(argname)
                    if pargs[position] < low or pargs[position] > high:
                        print('argument "{0}" not in <{1}:{2}>'.format(argname, low, high))
                        return None
                else:
                    print('Argument {} have a default value'.format(argname))
            return func(*pargs, **kargs)
        return onCall
    return onDecorator


@range_test_1((1, 0, 120))
def pers_info(name, age):
    print('{} is {} year old'.format(name, age))


@range_test_1_v2
def birthday(D: (1, 31), M: (1, 12), Y: (0, 2009)):
    print('Born {0}/{1}/{2}'.format(D, M, Y))


pers_info('Bob Smith', 45)
pers_info('Bob Smith', 200)

birthday(31, 5, 1963)
birthday(32, 5, 1963)
print()


@range_test_2(age=(0, 120))
def pers_info(name, age):
    print('{} is {} year old'.format(name, age))


@range_test_2(D=(1, 31), M=(1, 12), Y=(0, 2009))
def birthday(D, M, Y):
    print('birthday = {0}/{1}/{2}'.format(D, M, Y))


pers_info('Bob', 40)
pers_info(age=40, name='Bob')
pers_info('Bob', 150)
pers_info(age=150, name='Bob')
birthday(1, M=5, Y=1963)
birthday(40, M=5, Y=1963)
print()


@range_test_2(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def test(a, b=7, c=8, d=9):
    print(a, b, c, d)


test(1, 2, 3, 4)
test(1, 2, 3)
test(1, d=4)
test(1, 2, 11)
test(1, 2, 3, d=11)
