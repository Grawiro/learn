def potegowanie(c):
  if not hasattr(c,'__pow__'):
    def power(x,n):
      if (n<1):
        return x/power(x,-n+1)
      if n==1:
        return x
      if n%2:
        a=power(x,(n-1)/2)
        return x*a*a
      a = power(x,n/2)
      return a*a
    c.__pow__=power
  return c


@potegowanie
class Ulamek:

  def __init__(self,licznik,mianownik):
    self.l=licznik
    self.m=mianownik
    
  def __str__(self):
    return '%s/%s' % (self.l,self.m)
    
  def __mul__(self,drugi):
    return Ulamek(self.l*drugi.l,self.m*drugi.m)
    
  def __truediv__(self,drugi):
    return Ulamek(self.l*drugi.m,self.m*drugi.l)


print(Ulamek(2,3)**4)
print(Ulamek(2,3)**-2)
