###
# exceptions
###

print('its debug or not', __debug__, '\n')

# my exception class
class Error(Exception): pass
try:
    if 1==2:
        raise InterruptedError
    elif 1==3:
        raise Error()
    elif 1==4:
        # do only in debug/test mode no in final version
        # if use python -O basics.py in terminal assert have skip
        # assert False, 'this is error messenge'
        # or exception
        assert False, KeyboardInterrupt()
    elif 1==5:
        # if expect: they dont work, because when they close program they raise
        # exception/if defind finally do it and when close program
        # exit()
        quit()
    elif 1==6:
        # all exception class take *args
        raise Error('some', 'arguments', 'here', 342)
except (InterruptedError, StopIteration) as error:
    print('one of this')
    # raise this exception upper to other try-except block or return 
    # error and close program
    # raise
    # to raise two exception in one raise error and KeyError()
    raise KeyError() from error
except AssertionError as s:
    print('assert', s.args)
# as object, now can use object in expect and call variable and methods 
except Error as error:
    import sys
    print('My error from', error.__class__, 'or', sys.exc_info()[0])
    # print arguments
    print(error, error.args)
# this one catch all exception without system out exception like exit/quit
# except Exception:
except:
    print('unknow error')
else:
    print('no exception')
# can be only try-finally
finally:
    print('always will be done\n')

# use two or more context meneger
with open('temporary.txt', 'w') as file, open('temporary.txt', 'r') as file_r:
    file.write('tmp!\n')
    file.flush()
    print(file_r.read())
# the same
with open('temporary.txt', 'w') as file:
    with open('temporary.txt', 'r') as file_r:
        file.write('tmp!\n')
        file.flush()
        print(file_r.read())
# this the same but this is only one context meneger
myfile = open('temporary.txt')
try:
    for line in myfile:
        print(line)
finally:
    myfile.close()
# 

# this create local precision context
import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 2
    x = decimal.Decimal('1.00') / decimal.Decimal('3.00')
    print(x)
x = decimal.Decimal('1.00') / decimal.Decimal('3.00')
print(x, '\n')

# to use class in with need create __enter__/__exit__ method
class TraceBlock:
    def message(self, arg):
        print('do', arg)
    def __enter__(self):
        print('with starts')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('normal exit\n')
        else:
            print('exception', exc_type)
            # if False close program
            return True

with TraceBlock() as action:
    action.message('test 1')
    print('do it')

with TraceBlock() as action:
    action.message('test 2')
    if 1==1:
        raise TypeError
    print('never do it')
print('do it\n')

class Some_Error_1(Exception):
    def __str__(self):
        return 'This is my exception'
class Some_Error_2(Exception):
    def __init__(self, line, file):
        self.line=line
        self.file=file
        # can create methods
    def some_method(self):
        print('some_method')

try:
    if 1==2:
        raise Some_Error_1('my error')
    elif 1==1:
        raise Some_Error_2(119, 'basics.py')
except Some_Error_1 as error:
    print(error, error.args)
except Some_Error_2 as error:
    import sys
    # show active line and file when rise the exception
    import traceback
    print(traceback.print_exc(), sys.exc_info()[:2])
    print(error.args, error.line, error.file)
    error.some_method()