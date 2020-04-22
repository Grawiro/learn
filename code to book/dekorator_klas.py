def dekorator_ok(lancuch):
  def d(c):
    stary_init=c.__init__
    def nowy_init(*args):
      stary_init(*args)
      print('zostala stworzona nowa instancja')
    def ok(self):
      return lancuch
    c.ok=ok
    c.__init__=nowy_init
    return c
  return d

  
@dekorator_ok('Hello')
class Klasa:

  def __init__(self):
    print('teraz dziala konstruktor')


k=Klasa()
