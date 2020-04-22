def fibbg():
  a=1
  b=1
  while True:
    yield a
    a,b=b,a+b


licznik=0    
for i in fibbg():
  print(i)
  licznik+=1
  if licznik == 10:
    break
