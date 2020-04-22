def wypisz(c):
  if not hasattr(c,'__str__'):
    def str(self):
      return "Instancja klasy: %s" % self.__class__.__name__
    c.__str__ = str
  return c
  
  
@wypisz
class Klasa:

  def __str__(self):
    return 'ok'


k=Klasa()
print(k)

