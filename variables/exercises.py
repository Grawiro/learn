###
# exercises
###

# 1
text = 'something'
# empty
print(text[:0])

# 2
some_list = [0, 1, 2, 3]
# list index out of range
# print(some_list[4])
# will fit into the entire list
print(some_list[-1000:100])
# the second value can't be lower than the first, its changes into the first
some_list[3:1]=['?']
print(some_list)

# 3
# add empty list
some_list[3] = []
print(some_list)
# delete this
del some_list[3:]
print(some_list)
# the slice adopts sequential values
#some_list[:] = 1

# 4
# exchange of values ​​in places
y, z = 1, 2
print(y, z)
y,z = z,y
print(y, z)

# 9
# WTF!!!
s = 'foo'
print(s[0][0][0][0][0])
s = list('foo')
print(s[0][0][0][0][0])