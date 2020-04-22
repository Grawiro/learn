class Dekorator_ogolny:

  def __init__(self,lancuch):
    self.lancuch=lancuch
    
  def __call__(self,c):
    c.ok=lambda x:self.lancuch
    return c
    
    
class Dekorator_inf(Dekorator_ogolny):

  def __call__(self,c):
    super().__call__(c)
    stary_init = c.__init__
    def nowy_init(*args):
      stary_init(*args)
      print('zostala stworzona nowa instancja')
    c.__init__= nowy_init
    return c


@Dekorator_inf('Hello')
class Klasa:

  def __init__(self):
    print('teraz dziala konstruktor')


k=Klasa()
print(k.ok())
