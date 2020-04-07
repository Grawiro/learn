###
# if statement
###

# return first True or right argument
print(1 or 2, 1 or 0, 0 or 1, [] or {})
# return first False or right argument
print(1 and 2, 1 and 0, 0 and 1, [] and {})
# return a if True else b
print(1 if True else 0)
# the same what above if True 1 else 0
print(((True and 1) or 0))

###
# loops
###
i=0
while i<10:
    i+=1
    # ... (Ellipsis) is the same what pass, says fill this later, now do nothing
    if i==1:
        ...
    # skips the loop cycle
    if i==4:
        continue
    print(i, end='>')
    # finish the loop
    if i==7:
        print()
        break
# do it only if loop don't breaking
else:
    print(i)

# read file using iterators
for some_line in  open('../basics/data.txt', 'r'):
    print(some_line, end='')

# zip, connect the list by index
for x,y,z in zip([1,2,3], [3,2,1], [9,4,8]):
    print(x+y+z)

# both do the same
print(list(map(ord, ['a', 'b', 'c'])))
for x in map(ord, ['a', 'b', 'c']):
    print(x)

# create dict from lists
print(dict(zip(['a', 'b', 'c'], [1, 2, 3])))

# return index and element
for x,y in enumerate('some'):
    print(x,'->',y)

# iterate through the list
some_list = [1, 2, 3, 4]
some_iterator = iter(some_list)
while True:
    try:
        x = next(some_iterator)
    except StopIteration:
        break
    print(x)

# to iteration better use .__next__()
import os
some_iterator = os.popen('dir')
print(some_iterator.__next__())

# to connect list element in one element
import functools, operator
print(functools.reduce(operator.add, ['this', ' is ', 'some ','list']))

# return sum of each element
print(sum([1, 2, 3, 4]))
# return True if one element is true
print(any([1, 2, '3', '']))
# return True if all element is true
print(all([1, 2, '3', '']))
# return max and min (value or len char)
print(max([1, 2, 3, 4]))
print(min([1, 2, 3, 4]))

# connect all line in one string
some_text = '->'.join(open('../basics/data.txt'))
print(some_text)

# unzip tuple
some_tuple_1 = (1, 2)
some_tuple_2 = (3, 4)
some_tuple = zip(some_tuple_1, some_tuple_2)
print(list(some_tuple))
# this is nonsense, imo better use (some_tuple_1, some_tuple_2)
some_tuple = zip(*zip(some_tuple_1, some_tuple_2))
print(list(some_tuple))

some_dict = {'c':1, 'a':2, 'b':3}
print(some_dict)
for i in sorted(some_dict): print(str(i)+':'+str(some_dict[i]), end=', ')
print()

# return list of method and function
print(dir(functools))
# return documentation
print(functools.reduce.__doc__)
help(functools.reduce)
# this create html documentation file, use in terminal 
# python3 /lib/python3.7/pydoc.py -w basics/variables.py 