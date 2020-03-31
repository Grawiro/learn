###
# list
###

some_list = [3, 4, -1, 2, 5]
# add element to list
some_list.append(6)
some_list.extend([-8, -7, -9])
some_list.insert(0, 0)
print(some_list)

# remove elemet/s
del some_list[-1]
# remove last element
some_list.pop()
# or remove index
some_list.pop(1)
# remove element by value
some_list.remove(2)
# remove slice
some_list[:1] = []
print(some_list)

# modify the values ​​for sorting so that they are the same
some_list.sort(key=abs, reverse=True)
some_list = sorted(some_list, key=abs, reverse=False)
print(some_list)
some_list.reverse()
print(some_list)
print(some_list.count(5))
# what index is the value on
print(some_list.index(-1))
print(len(some_list))

print(3 in some_list)
for x in some_list:
    print(x, end=' ')

print('\n'+ str(list(map(abs, some_list))))

some_list = [0] * 5
print(some_list)

###
# dictionary
###

# create empty dictionary
some_dictionary = {}
some_dictionary['a'] = 'abc'
some_dictionary_check = some_dictionary.copy()
some_dictionary_check['b'] = 'xyz'
# add other dictionary
some_dictionary.update(some_dictionary_check)
# return keys/values/items
print(list(some_dictionary.keys()))
print(list(some_dictionary.values()))
print(list(some_dictionary.items()))
print('c' in some_dictionary)

some_dictionary_check = {
    'a': 'abc',
    'b': 'xyz',
    'c': 'cde'
    }
# remove keys
some_dictionary_check.pop('a')

try:
    print(some_dictionary_check['a'])
except KeyError:
    print("key doesn't exists")

# create new dictionary with keys and all have value
some_dictionary_check = dict.fromkeys(['a', 'b', 'c'], 0)
print(some_dictionary_check)
# zip combines values ​​from both lists in pairs
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
some_dictionary_check = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(some_dictionary_check)
some_dictionary_check = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(some_dictionary_check)