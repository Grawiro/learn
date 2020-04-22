def negacja(c):
  if not hasattr(c,'__neg__'):
    def __neg__(self):
      return self-self-self
    c.__neg__=__neg__
  return c


@negacja
class Liczba:

  def __init__(self,x):
    self.x=x

  def __str__(self):
    return str(self.x)

  def __sub__(self,drugi):
    return liczba(self.x-drugi.x)


l=Liczba(1)
print(-l)
