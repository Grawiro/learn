def mnozenie(c):
  if not hasattr(c,'__mul__'):
    def mul(x,n):
      if (n < 1):
        return x-mul(x,-n+1)
      if n==1:
        return x
      if n%2:
        a=mul(x,(n-1)/2)
        return x+a+a
      a = mul(x,n/2)
      return a+a
    c.__mul__=mul
  return c


@mnozenie
class Ulamek:

  def __init__(self,licznik,mianownik):
    self.l=licznik
    self.m=mianownik

  def __str__(self):
    return '%s/%s' % (self.l,self.m)

  def __add__(self,drugi):
    return Ulamek(self.l*drugi.m+drugi.l*self.m,self.m*drugi.m)

  def __sub__(self,drugi):
    return Ulamek(self.l*drugi.m-drugi.l*self.m,self.m*drugi.m)


print(Ulamek(2,3)*4)
print(Ulamek(2,3)*-2)
