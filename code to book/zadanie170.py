from math import atan2, cos, sin, pi

class Wektor:

  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __skaluj(self,v):
    r = (self.x**2+self.y**2)**.5
    self.x *= v/r
    self.y *= v/r

  def __obroc(self,v):
    r = (self.x**2+self.y**2)**.5
    self.x = r*cos(v)
    self.y = r*sin(v)   

  r = property(lambda self:(self.x**2+self.y**2)**.5,__skaluj)
  phi = property(lambda self:atan2(self.y,self.x),__obroc)

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
