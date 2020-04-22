class Klasa:

  def __init__(self):
    self.__x=1

  def x_czytaj(self):
    return 3*self.__x

  def x_zapisz(self,wartosc):
    if wartosc<1 and wartosc>0:
      self.__x=wartosc
    else:
      raise ValueError

  def x_usun(self):
    print('Nie mozna usunac')
    raise AttributeError

  x = property(x_czytaj,x_zapisz,x_usun)


k=Klasa()
k.x=.5
print(k.x)
del k.x
