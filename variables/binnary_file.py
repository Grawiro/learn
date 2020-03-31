###
# binary file
###
# open a binary file and read all and close
data = open('data.bin', 'rb').read()
finale_text = ''
comma=1
for element in list(data):
    finale_text += str(element)
    if comma == 8:
        comma=0
        finale_text+=','
    comma += 1
binary_list = finale_text.split(',')
binary_list = binary_list[:-1]
finale_text = ''
for element in binary_list:
    finale_text += chr(int(element, 2))
print(finale_text)