###
# tuple
###

# tuple with one element must have a comma
some_tuple = ('a',)
some_tuple = ('a', 'd', 'b', 'aa', 'c')
print(sorted(some_tuple))

###
# files
###

# w- write, r- read, rb -read binary, a- add to the end
some_file = open(r'data.txt', 'w', encoding='utf-8')
# write to file
some_file.write('line 1\nline 2\n')
some_file.write('line 3\tand line 3.5\n')
some_file.close()

some_file = open('data.txt', 'r')
# read 2 char with file
print(some_file.read(2))
print(some_file.readline())
print(some_file.readlines())
some_file.close()

# open read all and close
print(open('data.txt', 'r').read())
# the same
for line in open('data.txt', 'r'):
    print(line, end='')

save_list = [1, 2, 3]
save_text = 'some_text'
save_dict = {'a': 1, 'b': 2}
save_num = [5, 3, 34]
some_file = open('mix_data.txt', 'w')
some_file.write(save_text+'\n')
some_file.write('{}, {}, {}\n'.format(save_num[0], save_num[1], save_num[2]))
some_file.write(str(save_list)+';'+str(save_dict)+'\n')
some_file.close()

some_file = open('mix_data.txt', 'r')
# read text
read_text = some_file.readline().rstrip()
# read number
read_number = [int(x) for x in some_file.readline().split(',')]
# read list and dict
read_list = some_file.readline().rstrip().split(';')
read_dict = read_list[1]
read_list = read_list[0]
some_file.close()
print(read_text)
print(read_number)
print(read_list)
print(read_dict)

import pickle
some_pickle = open('data_pickle.pkl', 'wb')
# save variable in pickle file
pickle.dump(save_dict, some_pickle)
some_pickle.close()

some_pickle = open('data_pickle.pkl', 'rb')
# read var from pickle file
read_dict = pickle.load(some_pickle)
print(read_dict)

import struct
some_struct = open('data_struct.bin', 'wb')
some_struct.write(struct.pack('10s', 'to jest to'.encode()))
some_struct.close()

some_struct = open('data_struct.bin', 'rb')
print((struct.unpack('10s', some_struct.read()))[0].decode())
some_struct.close()

# to automaticly close file
some_file = open('data.txt', 'w')
try:
    some_file.write('this is good idea')
finally:
    some_file.close()
with open('data.txt', 'r') as some_file:
    for line in some_file:
        print(line)

###
# copy or reference
###

some_list = [1, 2, 3]
some_list_check = ['a', some_list, 'c']
some_dict = {'game': some_list, 'other': 34}
print(some_list, some_list_check, some_dict)
some_list[1] = 'this is reference'
print(some_list, some_list_check, some_dict)
some_list[1] = 2

# this is a copy
some_list_check[1] = some_list[:] 
some_dict['game'] = some_list.copy()
print(some_list, some_list_check, some_dict)
some_list[1] = 'this is copy'
print(some_list, some_list_check, some_dict)

# this is a copy module
import copy
some_list_check = copy.copy(some_list)
some_list_check = copy.deepcopy(some_list)

# value is the same, is a reference
print(some_list == some_list_check, some_list is some_list_check)