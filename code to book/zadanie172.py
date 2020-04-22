from math import atan2, cos, sin, pi


class Promien:

  def __get__(self,instancja,klasa):
    return (instancja.x**2+instancja.y**2)**.5

  def __set__(self,instancja,wartosc):
    r = (instancja.x**2+instancja.y**2)**.5
    instancja.x *= wartosc/r
    instancja.y *= wartosc/r


class Kat:

  def __get__(self,instancja,klasa):
    return atan2(instancja.y,instancja.x)

  def __set__(self,instancja,wartosc):
    r = (instancja.x**2+instancja.y**2)**.5
    instancja.x = r*cos(wartosc)
    instancja.y = r*sin(wartosc)   


class Wektor:

  def __init__(self,x,y):
    self.x=x
    self.y=y

  r=Promien()
  phi=Kat()

  def __delattr__(self,a):
    if a in ['x','y']:
      raise AttributeError
    super().__delattr__(a) # super bez self!
    
    
w=Wektor(0,1)
print(w.r, w.phi)
w.phi=pi/4
print(w.x, w.y)
w.r=2
print(w.x, w.y)
w.y=1
print(w.r, w.phi)
del w.x
