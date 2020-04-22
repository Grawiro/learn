class Zakres:

  def __init__(self,n):
    self.n=n
    self.i=0

  def __iter__(self):
    return self

  def __next__(self):
    if self.i==self.n:
      raise StopIteration
    r=self.i
    self.i+=1
    return r


for i in Zakres(4):
  print(i)
