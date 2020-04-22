def stos(l):
  s=None
  while True:
    x = yield s
    if x is None:
      try:
        s=l.pop()
      except:
        raise StopIteration from None
    else:
      s = None
      l.append(x)
           
           
s=stos([1,2,3])
s.send(None)

s.send('a')
s.send('b')
for i in s:
    print(i)
