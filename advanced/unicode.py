# -*- coding: utf-8 -*-
# change coding perhaps only in print

import sys
import encodings
import re
import struct
import xml.sax.handler
import xml.sax
from xml.etree.ElementTree import parse

# show default system encoding
print(sys.getdefaultencoding())

i = 1
while i < 55296:
    print('{:5}{:1}{:1}'.format(i, ':', chr(i)), sep='', end=' ')
    if not i % 12:
        print()
    i += 1

# show all encodings to use
help(encodings)

some_byte = b'some bytes text'
some_string = 'some string text'
print(some_byte, some_string)
# if take one elements from bytes return ASCII number
print(some_byte[0], some_string[0])
# change string to bytes and bytes to string
# if empty encoding in encode/decode Python use default utf-8
print(some_string.encode('utf-8'), '--', bytes(some_string, 'utf-8'))
print(some_byte.decode(), '--', str(some_byte, 'utf-8'), '\n')

# \x use 8 bits, \u use 16 bits, \U use 32 bits
some_string = '\x61\u0061\U00000061  \u00c4\U000000e8'
print(some_string, '--', some_string.encode())

# in ascii this is not display
print('뼃')

# this is a array/list of bytes
some_byte_array = bytearray(b'a')
print(some_byte_array, some_byte_array[0])
some_byte_array += b'b'
some_byte_array[0] = 99
some_byte_array.append(ord('a'))  # or 97
some_byte_array.extend(b' xyz')
print(some_byte_array)

some_string, some_byte, some_byte_array = 'abc', b'abc', bytearray(b'abc')
# this two is a list/set of ASCII char numbers
print(list(some_string), list(some_byte), list(some_byte_array), sep='\n')

# utf-8-sig use to open file write in utf-8 with BOM section

some_string = 'this is a short text to tests match'

print(re.match('this (.*) short (.*) to (.*)', some_string).groups())

# i-integer, s-bytes, number how many letters in string
some_value = struct.pack('i4si', 7, b'auto', 19)
print(some_value, struct.unpack('i4si', some_value), '\n')

# xml analise 3 version
# v1
xml_file = open('my_books.xml', 'r').read()
print(re.findall('<title>(.*)</title>', xml_file))


# v2
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False

    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True

    def characters(self, data):
        if self.inTitle:
            print(data)

    def endElement(self, name):
        if name == 'title':
            self.inTitle = False


parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('my_books.xml')

# v3
tree = parse('my_books.xml')
for element in tree.findall('title'):
    print(element.text)
