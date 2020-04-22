def wypisz(c):
  def str(self):
    return "Instancja klasy: %s" % self.__class__.__name__
  c.__str__ = str
  return c
  
  
@wypisz
class Klasa:
  pass
  
  
k=Klasa()
print(k)

