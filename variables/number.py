###
# numbers
###

# floating-point number (float)
3.14e-10
4e25
5.0e+30

# binary/octal/hexadecimal
print(0b0101,bin(30))
print(0o631,oct(190))
print(0xF2A,hex(152))
# convert to int 
print(int('772', 8))

# complex number
print(3+4j, 5j, complex(2, 3))

# conditional expression
3 if not (3==4) or 3!=4 and 3>=2 else 4
3 < 4 <= 4.5 > 4.25
# is (x in y)

# or x|y (sum of both set)
# xor x^y (difference)
# and x&y (part of the common)
# not ~x

# bit shift to the left
print(2<<2)

# power **
# modulo %
# division /
# floor division //

# ???
(...)
[...]
{...}

# Send generator function protocol (yield)
# lambda args: expression

# power
pow(2,4)
# absolute
abs(-8)
round(3.2)
# what numbers need to be divided to get value
print(0.5.as_integer_ratio())
print(3.2.is_integer())
some_number=8
print(some_number.bit_length())

# casting to integer
int(3.1415)
# casting to float
float(3)

# print various formats
print('{0:4.17f}'.format(2/3))
print('%e' % (2/3))
print('%4.2f' % (2/3))
# dec/oct/hex/bin
print('{:d}, {:o}, {:x}, {:b}'.format(64, 64, 64, 64))

# different methods display
print(repr(1/3),str(1/3))

import math
# the l2 places after the dotast example rounds to two places after the dot
print(round(2.3), round(2.9), round(-2.3), round(-2.9), round(2.567, 2))
print(math.floor(2.3), math.floor(2.9), math.floor(-2.3), math.floor(-2.9))
print(math.ceil(2.3), math.ceil(2.9), math.ceil(-2.3), math.ceil(-2.9))
# trims the fractional part
print(math.trunc(2.3), math.trunc(2.9), math.trunc(-2.3), math.trunc(-2.9))

print(3//2, math.trunc(-3/2))

print(2**2)

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), sum((1,2,3,4,5)))
print(min(3,2,1,4,5), max(3,2,1,4,5))

import random
# choose number from 0 to 10
print(random.randint(0,10))

# fixed integer precision
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
print()

###
# set
### 

some_set = {'a', 'b', 'c'}
some_set_check = {'a','c'}
print('a' in some_set)
# set 1 is all in set 2
print(some_set > some_set_check)
# set 2 is all in set 1
print(some_set < some_set_check)
# some methods
some_set_check.add('e')
some_set.remove('b')
some_set.update({'g', 'y'})
for item in some_set:
    print(item)
print(some_set.union([3, 4]))
print(some_set.intersection(('a', 'g', 'z')))
print(some_set.issubset(range(-5, 5)))

some_set = {x for x in [1, 2, 3, 4]}
some_set = {x for x in 'something'}
print(some_set)

###
# copy
###

import copy
some_list = [1, 2, 3, 4]
# default its the same list
some_list_check = some_list
some_list[0] = 0
print(some_list, some_list_check)
some_list_check = copy.deepcopy(some_list)
some_list[0] = 1
print(some_list, some_list_check)

###
# number of references to the variable
###

import sys
print(sys.getrefcount(1))