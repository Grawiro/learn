class Metoda:

  def __get__(self,instancja,klasa):
    def domkniecie(*args):
      return klasa.__dict__['_'+self.__class__.__name__](instancja,*args)
    return domkniecie

class Klasa:

  def _Metoda(self,x):
    return x
    
  metoda=Metoda()


print(Klasa().metoda(2))
