#!/usr/bin/python3
from requests import get
from sys import argv


def stolica(s):
  f=get('http://pl.wikipedia.org/wiki/'+s,stream=True)
  b,c='',''
  for l in f.iter_lines():
    a,b,c = (b,c,l.decode('UTF-8'))
    if 'Stolica</a>' in a:
      f.close()
      return c.split('">',1)[1].split('<',1)[0]
  f.close()


if __name__=='__main__':
  for i in argv[1:]:
    print(stolica(i.strip()))

