class Ulamek:

  def __init__(self,l,m):
    self.l=l
    self.m=m

  def __add__(self,drugi):
    if isinstance(drugi,Ulamek):
      return Ulamek(self.l*drugi.m+drugi.l*self.m,self.m*drugi.m)
    else:
      return Ulamek(self.l+drugi*self.m,self.m)

  def __sub__(self,drugi):
    if isinstance(drugi,Ulamek):
      return Ulamek(self.l*drugi.m-drugi.l+self.m,self.m*drugi.m)
    else:
      return Ulamek(self.l-drugi*self.m,self.m)

  def __mul__(self,drugi):
    if isinstance(drugi,Ulamek):
      return Ulamek(self.l*drugi,self.m*drugi.m)
    else:
      return Ulamek(self.l*drugi,self.m)

  def __truediv__(self,drugi):
    if isinstance(drugi,Ulamek):
      return Ulamek(self.l*drugi.m,self.m*drugi.l)
    else:
      return Ulamek(self.l,self.m*drugi)
  
  __radd__=__add__
  __rmul__=__mul__
  
  def __rsub__(self,drugi):
    return Ulamek(-self.l+drugi*self.m,self.m)

  def __rtruediv__(self,drugi):
    return Ulamek(self.m*drugi,self.l)
  
  def __str__(self):
    return '{0.l}/{0.m}'.format(self)
  
  def __int__(self):
    return self.l//self.m
