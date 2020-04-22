def stos(l):
  def wew(x=None):
    if x==None:
      try:
        return wew.l.pop()
      except:
        raise StopIteration from None
    else:
      wew.l.append(x)
  wew.l=l
  return wew

s=stos([1,2,3])
for i in 'Ala':
  s(i)
while True:
  print(s())
