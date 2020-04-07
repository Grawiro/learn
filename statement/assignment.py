###
# assignment
###

# instead of a list, there may be another type
some_list = [1,2,3,4]
# assign the element to the variable and the rest to the one with the star
a, *b = some_list
print(a,b)
# assign the last element
*a, b = some_list
print(a,b)
# assign the first and last element
a, *b, c = some_list
print(a,b,c)
# if nothing is left, the variable with an asterisk will get an empty list 
a, b, c, d, *e = some_list
print(a,b,c,d,e)

# print text to file 
some_file = open('../basics/data.txt', 'w')
print('file, file, file', file=some_file)
some_file.close()
print('to file again.',end='',file=open('../basics/data.txt', 'a'))
print(open('../basics/data.txt', 'r').read())

import sys
# both do exactly the same
sys.stdout.write('this is print function'+' '+'in construction'+'\n')
print('this is print function', 'in construction')

std_out = sys.stdout
sys.stdout = open('../basics/data.txt', 'w+')
print('text to file')
sys.stdout.close()
# both recover the defoult stdout, imho secound better
sys.stdout = std_out
#sys.stdout = sys.__stdout__
print('now normal')
print(open('../basics/data.txt', 'r').read(), end='')