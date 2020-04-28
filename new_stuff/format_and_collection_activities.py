import itertools

# new format string
a, b, c, text = 'first', 'last', 8, 'string'
print(f'{a} is not a  {b} or "{c}" and text\n{text}')

# combination and permutation
str_list = ['a', 'b', 'c']
print(list(itertools.combinations(str_list, 2)))
print(list(itertools.permutations(str_list, 2)))
