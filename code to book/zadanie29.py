def Horner(l,x):
  return reduce(lambda a,b:x*a+b,l[::-1])
  