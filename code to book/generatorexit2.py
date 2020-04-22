def suma():
  s=0
  while True:
    try:
      x=yield s
      x=float(x)
      s+=x
    except:
      pass
      
s=suma()
s.send(None)
s.send(1)
s.send(2)
s.send(3)
print(s.__next__())
