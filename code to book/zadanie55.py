# Nowy konstruktor w klasie Ulamek:

  def __init__(self,l,m):
    if type(l)!=int or type(m)!=int:
      raise TypeError
    if m==0:
      raise ZeroDivisionError
    self.l=l
    self.m=m
  
