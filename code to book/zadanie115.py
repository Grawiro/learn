class Zakres:
  
  def __init__(self,n):
    self.n=n
    
  def __getitem__(self,i):
    if i<self.n:
      return i
    else:
      raise IndexError

for i in Zakres(10):
  print(i)
