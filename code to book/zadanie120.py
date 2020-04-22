def primesg(n):
  t=[True]*n
  p=2
  while True:
    yield p
    i=p
    while i*p<n:
      t[i*p]=False
      i+=1
    while True:
      p+=1
      if p==n or t[p]:
        break
    if p==n:
      break


for i in primesg(100):
  print(i)
