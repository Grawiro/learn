class Fibb:

  def __init__(self):
    self.a = 0
    self.b = 1
    
  def __iter__(self):
    return self
    
  def __next__(self):
    self.a,self.b = self.b,self.a+self.b
    return self.a
    
licznik=0    
for i in Fibb():
  print(i)
  licznik+=1
  if licznik == 10:
    break
