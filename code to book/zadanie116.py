from time import time


class Timeint:

  def __init__(self):
    self.t = time()

  def __iter__(self):
    return self

  def __next__(self):
    t = time()
    self.t,t = t,t-self.t
    return t


T=Timeint()    
for i in range(10):
  print(next(T))
    
