#!/usr/bin/python3
from sys import argv
from subprocess import check_output

if len(argv)>1:
  s=argv[1]
  if not s.endswith('/'):
    s+='/'
else:
  s=''

s=check_output('du -s {0}* | sort -hr'.format(s), shell=True)[:-1]
s=s.decode('utf8').split('\n')
s=[i.split('\t') for i in s]
s=[(int(i[0]),i[1].rsplit('/',1)[-1]) for i in s]
r=0
while (len(s)>2) and s[-1][0]+r < s[0][0] and s[-1][0]<s[0][0]/40:
  r+=s.pop()[0]
if r:
  s.append((r,'reszta'))
s=[(i[0]*40//s[0][0]*chr(9617),i[1]) for i in s]
s='\n'.join(map(lambda i:'{0:<40s} {1:s}'.format(*i),s))
print(s)
