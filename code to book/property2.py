class Klasa:

  def __init__(self):
    self.__x=1

  @property
  def x(self):
    return 3*self.__x

  @x.setter
  def x(self,wartosc):
    if wartosc<1 and wartosc>0:
      self.__x=wartosc
    else:
      raise ValueError

  @x.deleter
  def x(self):
    print('Nie mozna usunac')
    raise AttributeError


k=Klasa()
k.x=.5
print(k.x)
del k.x
