###
# moduls
###

import sys
# return all import modules
print(sys.modules.keys())
print()
# add path to search imports module is only temporary.  this is relative path
# if run module with another path or import this module, this path doesnt work,
# unless an absolute path is given
# sys.path.append('../basics')
# like this
# sys.path.append('/home/grawiro/Documents/Python/nauka/book')
# or add a path relative to this file 
sys.path.append(__file__[:-17])
# or add path in file .pth in this directory
# /home/grawiro/.local/lib/python3.7/site-packages/
# this return all search paths to imports
print(sys.path)
print()

# from copy
# import original

# this close import file
del sys

# add other name to import module
import basics.file_to_import as file_to_import
# this reload import file 
from importlib import reload
reload(file_to_import)
print(file_to_import.title_1)

# import to_import_1.to_import_2.file_to_import
# from to_import_1.to_import_2  import file_to_import
# both the same
import to_import_1.to_import_2.file_to_import as file_to_import_2
file_to_import_2.show_x()
file_to_import_2.x = 99
file_to_import_2.show_x()
# must be full path when import without as
# to_import_1.to_import_2.file_to_import.show_x()
# this work only from import without as
#print(to_import_1.var_from_init)

# this import only define var and function
from file_to_import_all import *
print(var_2)
# this import few variables or functions
from file_to_import_all import _var_1, var_3
print(_var_1, var_3)

module_name = 'math'
# import module by variable value (string)
math = __import__(module_name)
# the same but __import__ better imho
# exec('import '+module_name)
print(math.sqrt(4))
print()

# reload only this module if import with from this method not working good, must
# again import this variable or function and import module before reload
reload(file_to_import_2)
print()
import reloadall
# reload all module in this module
reloadall.reload_all(file_to_import_2)