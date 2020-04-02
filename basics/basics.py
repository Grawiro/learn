###
# basics
###

# change coding system must be in first line
# coding: ISO-8859-2
print("ąęśćłńóżź")

some_var = 3
print(type(some_var))

# complex type
some_complex = 3.2+2.3j
# conjugate returns the number conjugated to some...
print(some_complex, some_complex.conjugate())

# encode only non-ascii characters
some_text = 'słoń'.encode('utf-8')
print(some_text)
print(some_text.decode('utf-8'))

# folded list with condition
print([i**2 for i in range(20) if i%2==1])
# double loop, the expression will be executed as if inside a loop
print([10*i+j for i in range(1,10) for j in range(1,i)], "\n")

some_global_var = 0
# args and kwargs (keys arguments), arguments list in function
def some_function(*args, **kwargs):
    '''this is documentation of what the function does'''
    print(args)
    print(kwargs)
    # use the global var in this function
    global some_global_var
some_function(1,2,a=1,b=2)
# show function documentation
print(some_function.__doc__)
print(abs.__doc__)

# anonymous function (lambda)
power = lambda a ,n=2: a**n
print(power(2,3))
some_function = lambda *args: (max(args)-min(args))/len(args) if args else None
print(some_function(1, 2, 3, 4))

some_list = [1,  2, 3, 4]
# (map) take another item from the list and add it as an argument to function
print(list(map(power, some_list)))
# the same but here lamba is temporary
print(list(map(lambda a: a**2, some_list)))
# leave only those that match
print(list(filter(lambda x: not x%2, some_list)))

some_list = [[3,1],[2,4]]
# sort by secound value in sub lists
print(sorted(some_list, key=lambda x:x[1]))

# to use reduce, takes two argumernt, and calculate [[[0]*[1]]*[2]]*[3] e.t.c.
import functools
# factorial calculation function
print(functools.reduce(lambda x,y: x*y, range(2,6)))
print(functools.reduce(lambda x,y: x+[x[-1]*y], range(2,6), [1]))

if __name__=='__main__':
    print('do it only if this is a main file')

from sys import argv
print(argv)
# you can add some parameters after the file name
# python3 basics.py arguments other

# exception
try:
    y=1/0
except ZeroDivisionError:
    print('division by zero')
except KeyboardInterrupt:
    print('ctrl+c')
except:
    print('catch all exception')
else:
    print('all right')
finally:
    print('will always be done')

# file
# r-read/w-write/c-create/b-beginning/e-end/d-delete data/ce-if exists return error
# "r"[r,b]
# "a"[w,e,c]   "a+"[rb,we,c]
# "w"[w,b,c,d]
# "x"[w,b,ce]
# "-+"[w,r]"w+"
# "b-"[binnay mode]"br"

# name and open mode the file
# file.mode
# file.name

# good counting time
from time import time

now_time= time()
pow(2,1000000)
print('{:.2f}s'.format(time()-now_time))

now_time= time()
pow(2,20000000)
print('{:.2f}s'.format(time()-now_time))

# date
import datetime
print(datetime.date.today(), datetime.date.today().weekday()+1,
    datetime.datetime.now())
print(datetime.date(2000,2,11), datetime.time(8,53,20,3243))

# executes a system command
import subprocess
subprocess.Popen('echo "xxx">a.txt', shell=True)
# returns a byte string after the command has been completed
print(subprocess.check_output('cat a.txt', shell=True))

# os function
import os
print(os.listdir())

# get the html from some site
from requests import get
some_site = get ('http://docs.python.org')
some_text = some_site.text
some_site.close ()
print(some_text)

# get line by line
some_site = get('http://docs.python.org', stream=True)
for i in some_site.iter_lines():
    print(i.decode())
some_site.close()

# similar to above
from urllib.request import urlopen
some_site = urlopen('http://docs.python.org')
some_text=some_site.read()
print(len(some_text))
some_site.close()




















