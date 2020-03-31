###
# This is a first file, I write after a break.
###

# Python philosophy
import this

print("\nhello world")

# 2 to the power of 100/two to the hundredth power
print(2**100)

# duplicate text 3 times
print('something'*3, "\n")

# checks the platform, where works
import sys
print(sys.platform, "\n")

import file_to_import 
# importlib is a new version imp library
from importlib import reload
# function to reload import file (again import)
reload(file_to_import)
# use the attribute from the file_to_import module
print(file_to_import.title_1, "\n")
# show all variables in file_to_import
print(dir(file_to_import), "\n")

# copy only title from file_to_import
# from file_to_import import title_1
# copy all from file_to_import
# from file_to_import import *
# can use all without (.), because it's no longer an attribute, but a variable
# print(title_1)

import os
# shows files and directories in the current directory
print(os.listdir(), "\n")
# run the file
exec(open('file_to_import.py').read())
print()

###
# exercises
###

some_list = [
    1,
    2,
    ]
# creates infinitely nested arrays
some_list.append(some_list)
print(some_list)
print(some_list[2][2][0])

###
# I won't know for a long time.
###

# some function
# import os
# os.getcwd()

# to run system command
# os.system

# probably to run the program
# os.popen