###
# strings
###

# raw string
some_string = r'\t\n /usr/bin'
# binary string
some_string = b'something'
some_string = 'something'
# ends with ...
print(some_string.endswith('ing'))
# start with ...
print(some_string.startswith('some'))
# changes the character encoding
some_string.encode('latin-1')
for x in some_string:
    print(x, end='-')

# display ascii code
print('\n'+ str(list(map(ord, some_string))))

print('ing' in some_string)
# ::step
print(some_string[::2])
# ord return ascii code, chr return char
print(ord('a'), chr(97))

# to replace something
some_list = list(some_string)
some_list[0] = 'm'
some_list[1] = 'a'
# joins columns into text, with such '' a limiter, may be different
some_string = ''.join(some_list)
print(some_string)

some_string = '{0} and {food}'
some_string = some_string.format('ham', food='eggs')
print(some_string)

import sys
print('On my {config[spam]} is {sys.platform}'.format(
    sys=sys, config={'spam': 'laptop'}))
# </>/=/^ align, only 0 filling, 10 characters, .3f number after dot
# , thousands separator
print('{:^13}, {:010.1f}, {:5,}'.format(123,13.231321,14212))

# reverse
print(some_string[::-1])