class Primes:

  def __init__(self,n):
    self.n=n
    self.t=[True]*n
    self.i=1

  def __iter__(self):
    return self

  def __next__(self):
    if self.i>1:
      i=self.i
      while i*self.i<self.n:
        self.t[i*self.i]=False
        i+=1
    while True:
      self.i+=1
      if self.i==self.n:
        raise StopIteration
      if self.t[self.i]:
        break
    return self.i


it=Primes(100)
for i in it:
  print(i)
