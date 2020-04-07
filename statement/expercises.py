###
# exercises
###

# 1
some_list = ['a', 'b', 'c']
expect = [ord(x) for x in some_list]
print(expect)
expect = list(map(ord, some_list))
print(expect)
expect = sum(list(map(ord, some_list)))
print(expect)

# 4
some_list = [2**i for i in range(9)]
print(some_list)
print(some_list.index(2**5) if 2**5 in some_list else 'not found' )