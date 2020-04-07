###
# functions
###

# all built name in python
import builtins
print(dir(builtins))

def function(y):
    # x is global var, y is local var 
    return x+y

def function_2(y):
    # x is local var
    x = 88
    return x+y

def function_3(y):
    # get the global var or create a global var
    global x 
    x = y
    global f 
    f = 12
    return x + y

# import self to change global var
def function_4():
    import functions
    functions.x = 9

x = 99
some_function = function
print(some_function(1), x)
print(function_2(1), x)
print(function_3(1), x, f)

# this function return other function
def function_5(x):
    # this function remember the above function argument
    def function_6(y):
        return y**x
    return function_6

some_function = function_5(2)
print(some_function(4))

# lambda, imho better use only lambda
def function_6(x):
    # default value, not necessary
    return lambda z, x=x: z**x

some_function = function_6(3)
print(some_function(3))

# use var from above function, must exists
def function_7(x):
    def function_8(y):
        nonlocal x
        x+=1
        # function_8.z is a local var create in global state
        function_8.z+=1
        return y+' '+str(x)+' '+str(function_8.z)
    return function_8
    
some_function = function_7(0)
some_function.z=9
print(some_function('a'))
print(some_function('b'))

# 1 is a orginal list rest is a copy, list and dict is mutable
def function_8(some_list_1, some_list_2, some_list_3, some_list_4):
    some_list_1[0] = 8
    some_list_2 = some_list_2[:]
    some_list_2[1] = 7
    some_list_3[2] = 6
    some_list_4[3] = 5

some_list = [1, 2, 3, 4]
# 3 and 4 handing over a copy
function_8(some_list, some_list, some_list[:], some_list.copy())
print(some_list)

def function_9():
    return 3, [1, 2]
# function change value of var
x, some_list = function_9()
print(x, some_list)

# default value
def func_1(a, b=9):
    print(a,b)
    print(a+b)
# *list, **dict unzip to single element or in dict only value
func_1(*some_list)
some_dict = {'a':1, 'b':2}
func_1(**some_dict)
# call with default value
func_1(1)
# call with name=value
func_1(b=3, a=2)
# get the all argument in one tuple and one dict
def func_2(*args, **kwargs):
    print(args)
    print(kwargs)
# **dict unzip to pairs (key, value)
func_2(*some_list, '3', **some_dict, e=4, z='y')

# this is keywords-only must call with name=value, may have a default value
def func_3(*, a, b=2):
    print(a, b)
func_3(a=1,b=2)
func_3(a=1)

# order of arguments
def func_4(first, second='sec', *args, keyword, sec_keyword='def', **kwargs):
    print(first, second)
    print(keyword, sec_keyword)
    print(args, kwargs)

func_4('first', 'sec', 'arg', 'args', keyword='must be', sec_keyword='can skip',
    some_key='kwargs', another_key='and', number=25)


def search_min(*args):
    result = args[0]
    for tmp in args[1:]:
        if tmp<result:
            result=tmp
    return result
# both the same
def search_min_2(*args):
    result = list(args)
    result.sort()
    return result[0]

print(search_min([1,2,3], [1,2], [1,2,3,4]))
print(search_min([3,3], [2,2], [1,1]))
print(search_min(4, 1, 3, 2))