###
# continue function
### 

# function call self
def recursion_sum(some_list):
    print(some_list)
    if not some_list:
        return 0
    return some_list[0]+recursion_sum(some_list[1:])

print(recursion_sum([1,2,3,4,5]))

# annotations: expected values or return type (int)
def recursion_sum_2(some_list: 'list') -> int:
    result = 0
    for x in some_list:
        if isinstance(x, list):
            result += recursion_sum_2(x)
        else:
            result += x
    return result

print(recursion_sum_2([1,[2,[3,4],5],6,[7,8.1]]))
print(recursion_sum_2.__annotations__)

import sys
some_lambda = lambda x: [sys.stdout.write(i) for i in x]
some_lambda(['this', ' is ', 'some text\n'])
some_lambda = (lambda x: lambda y: x+y)(1)
print(some_lambda(2))
print((lambda x: lambda y: x+y)(1)(2))

print(list(map(pow, [1,2,3,4],[1,2,3,4])))
print(list(filter((lambda x: x > 0), range(-5, 5))))
from functools import reduce
print(reduce((lambda x, y: x+y), [1, 2, 3, 4]))
from operator import add
print(reduce(add, [1, 2, 3, 4]))

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

M = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print([row[0] for row in M])
print([M[row][1] for row in (0, 1, 2)])
print([M[i][i] for i in range(len(M))])

# yield return a partial result, is a iterable function
def gen_power(x):
    for i in range(x+1):
        yield i**2

for i in gen_power(5):
    print(i, end=', ')
print()

def gen_power_2(x):
    stop=''
    for i in range(x+1):
        if stop=='stop':
            break
        # return value and if next time send value assign to variable
        stop = yield i**2
        if stop is None:
            stop=''

for i in gen_power_2(5):
    print(i,end='. ')
print()

try:
    # create genarator
    some_generator = gen_power_2(5)
    # return value and nothing send
    print(some_generator.__next__(), end='/')
    # return value and send None
    print(some_generator.send(None), end='/')
    # send 'stop' and break function
    print(some_generator.send('stop'))
# if break function raise exception
except StopIteration:
    print()

print()

# this is a comprehension list
print([2**x for x in range(5)])
# this is a generator 
some_generator = (2**x for x in range(5))
print(some_generator.__next__(), end=', ')
print(some_generator.__next__(), end=', ')
print(some_generator.__next__(), end=', ')
print(some_generator.__next__())

def func(*args, empty=None):
    x,y = len(args[0]), len(args[1])
    if x < y:
        z_1=args[0][:]+[empty]*(y-x)
        return zip(z_1, args[1])
    elif x > y:
        z_2=args[1][:]+[empty]*(x-y)
        return zip(args[0], z_2)

print(list((func([1,2], [1,2,3,4,5], empty='emp'))))

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

print(mymapPad([1,2,3,4], [1,2], pad='emp'))

# comprehesion dictionary
{x: x * x for x in range(10)}

###
# common mistakes
### 

some_list = [1,2,3,4]

def function_1():
    # to use global and local variable in function, at the same time
    import __main__
    print(__main__.some_list)
    some_list = [1,2,3,4,5,5,6,7]
    print(some_list)

function_1()
print(some_list)

# mutable default value
def function_2(*, some_list=[0]):
    some_list.insert(0 ,some_list[0]+1)
    some_list.pop(1)
    print(some_list[0])

function_2()
function_2()