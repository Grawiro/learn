from requests import get
from time import time


def stolica1(s):
  f=get('http://pl.wikipedia.org/wiki/'+s)
  s=f.text
  f.close()
  return s.split('Stolica</a>',1)[1].split('">',1)[1].split('<',1)[0]

  
def stolica2(s):
  f=get('http://pl.wikipedia.org/wiki/'+s,stream=True)
  b,c='',''
  for l in f.iter_lines():
    a,b,c = (b,c,l.decode('UTF-8'))
    if 'Stolica</a>' in a:
      f.close()
      return c.split('">',1)[1].split('<',1)[0]
  f.close()


kraje=['Polska','Litwa','Łotwa','Estonia','Finlandia','Szwecja','Norwegia','Islandia']

t=time()
list(map(stolica1,kraje))
print(time()-t)
t=time()
list(map(stolica2,kraje))
print(time()-t)

