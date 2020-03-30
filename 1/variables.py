###
# variables
###

###
# numbers 
###

print(123 + 222)
print(1.5 * 4)
print(2 ** 8)
# how many numbers will be after this operation
print(len(str(2 ** 1000000)))
print(3.1415 * 2, "\n")
# imports mathematical functions
import math
print(math.pi)
print(math.sqrt(85), "\n")
# imports random functions
import random
print(random.random())
# chooses one value from the list
print(random.choice([1, 2, 3, 4]), "\n")

###
# strings
###

some_text = "something"
print(some_text+ ", lenght =", len(some_text))
# select one character
print("char 1 =", some_text[0]+ ", char 2 =", some_text[1])
# select from the end
print("last char =", some_text[-1]+ ", char before last =", some_text[-2])
# select one character another option 
print("select one character =", some_text[len(some_text)-1])
# select slice from x to y-1
print("0:3="+some_text[:4]+ ", 3:5=" +some_text[3:6]+ ", 5:-1="+some_text[5:])
# string is immutable, to change something need to create new string
some_text = "t" + some_text[1:]
print(some_text+"\n")

# method find, return index or -1 if not find
print(some_text.find("th"))
# method to replace the slice another string, how much to replace
print(some_text.replace("me", "r", 1), "\n")

another_text = "aaa,bbb,cccc,dd\n"
# split string into list by delimiter
print(another_text.split(","))
# to uppercase, or to lowercase
print(some_text.upper(), some_text.lower())
# is number, or is a string
print(some_text.isdigit(), some_text.isalpha())
# deletes the whitespaces rstrip/lstrip/strip - right/left/both
print(another_text.rstrip())
# format replace {}
print("{} and {}".format("cheese", "ham"))
print("{1} and {0}".format("cheese", "ham"), "\n")

# return all method from variable
print(dir(some_text), "\n")
# display information about method
# help(some_text.replace)

# \n-new line \t-tab \r-carriage return \a-bell \b-backspace
another_text = "A\tB\nC\rD"
print(another_text)
# ord return value of ascii
print(ord("a"))
# \0 is a byte zero, not display, but is counted
another_text = "A\0B\0C"
print(another_text, "\n")
another_text = '''multiline text'''

# match to the pattern 
import re
match = re.match("Hello,[ \t]*(.*)Robinie", "Hello, sir Robinie")
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/grawiro')
print(match.groups(), "\n")

###
# list/array
###

some_list = [
    123,
    'abc',
    1.23
    ]
# remove last/specific item from list
some_list.pop()
# remove item by value
some_list.remove(123)
# add value to list end
some_list.append('xyz')
# add item to specific index in list
some_list.insert(2,'cat')
# reverse list
some_list.reverse()
# sort list a to z
some_list.sort()
print(some_list, "\n")

# nested list
some_nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]
print(some_nested_list)
print(some_nested_list[1][1], "\n")

# list comprehension
# select row[2] (value + operations) from nested list
col = [row[2] for row in some_nested_list]
print(col)
print(list(row[2] for row in some_nested_list))
print(list(row[2] for row in some_nested_list if row[2] % 2 == 1))
# select specific item from nested list here diagonal
print(list(some_nested_list[i][i] for i in [0, 1, 2]))
# use the for loop
print(list(i for i in 'text'))
# sum all value in row
some_sum_generator = (sum(row) for row in some_nested_list)
print(next(some_sum_generator), next(some_sum_generator))
# the same
print(list(map(sum, some_nested_list)))
# create list/set/dictionaries 
some_dictionaries = {i : sum(some_nested_list[i]) for i in range(3)}
print(some_dictionaries)
print(list(ord(i) for i in 'text'))
print(set(ord(i) for i in 'text'))
print(dict({i: ord(i) for i in 'text'}), "\n")

###
# dictionaries
###

some_dictionaries = {}
some_dictionaries["last_name"] = "ppp"
print(some_dictionaries)

# create nested dictinaries
some_dictionaries = {
    "personal data":{
        "first_name" : "kamil",
        "last_name" : "pp",
        },
    "nickname" : [
        "grawiro",
        "purcus00",
        ],
    "age" : 19,
    }
some_dictionaries["age"] += 1
some_dictionaries["nickname"].append("mistic")
print(some_dictionaries)
print(some_dictionaries["personal data"]["first_name"])
print(some_dictionaries["nickname"][0])

# how sort dictionaries
some_dictionaries_sort = list(some_dictionaries.keys())
some_dictionaries_sort.sort()
for key in some_dictionaries_sort:
    print(key, "=>", some_dictionaries[key])
# the same but better
for key in sorted(some_dictionaries):
    print(key, "=>", some_dictionaries[key])
print()

# if key not exist
# in return True or False
print('key' in some_dictionaries)
# more advanced, all it the same
if not 'key' in some_dictionaries:
    print("this key not exist")
print(some_dictionaries.get('key', 'this key not exist'))
print(some_dictionaries['key'] if 'key' in some_dictionaries else 'bad key', "\n")

###
# loops
###

for i in 'text':
    print(i, end='=>')
print()

i = 1
while i <= 3 :
    print('*' * i)
    i += 1
print()

###
# tuple
###

# tuple is immutable
some_tuple = ("a", 'b', 4)
some_tuple = some_tuple + (5, 'a', 3)
print(some_tuple)
# how many times the value is in the tuple
print(some_tuple.count('a'))
# return value index from tuple
print(some_tuple.index(3))

###
# files
###

# create and open file to write
some_file = open('1/data.txt', 'w')
# write something to file
some_file.write('Hello,\n')
some_file.write('Kamil.\n')
# file must be close
some_file.close()

# open file to read
some_file = open('1/data.txt', 'r')
# read all data from file, type is always string
some_text = some_file.read()

print(some_text)
some_file.close()

# open a binary file and read all and close
data = open('1/data.bin', 'rb').read()
print(data)

###
# sets
###

# string to set
some_set = set('something')
some_set_check = {
    'a', 'b', 
    'e', 't', 
    'h', 'i', 
    'j'
    }
# part of the common
print(some_set & some_set_check)
# sum of both set
print(some_set | some_set_check)
# difference
print(some_set - some_set_check, "\n")

###
# decimal numbers
###

print(1/3, (2/3) + (1/2))

# advanced decimal number
import decimal
some_decimal = decimal.Decimal('3.141')
print(some_decimal+1)
# set the precision
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))
# set the local precision
with decimal.localcontext() as ctx:
    ctx.prec = 6
    print(decimal.Decimal('1')/decimal.Decimal(str(3)))

print(decimal.Decimal('1')/decimal.Decimal('3'))

# advanced fractions
from fractions import Fraction
some_fractions = Fraction(2, 3)
print(some_fractions + 1)
print(some_fractions + Fraction('1.5'))
# other method to create fractions
some_fractions = Fraction.from_float(1.75)
some_fractions = Fraction(*(1.75).as_integer_ratio())
# convert to float
print(float(some_fractions))
# simplification to the nearest fraction good to big number
some_fractions.limit_denominator(10)
print(some_fractions)

###
# other type and checks type
###

# None type
some_none = None
print(some_none)
# check type
print(type(some_none))

if isinstance(some_list, list):
    print("some_list is a list")


###
# class
###

# create class
class Worker:
    # initialization class
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    # self must be
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0+percent)

worker_bob = Worker('Bob Smith', 5000)
worker_bob.giveRaise(.35)
print(worker_bob.lastName(), worker_bob.pay)