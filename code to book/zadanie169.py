from math import atan2, cos, sin, pi


class Wektor:

  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __getattr__(self,a):
    if a=='r':
      return (self.x**2+self.y**2)**.5
    if a=='phi':
      return atan2(self.y,self.x)
    raise AttributeError

  def __setattr__(self,a,v):
    if a=='r':
      r = (self.x**2+self.y**2)**.5
      self.x *= v/r
      self.y *= v/r
    elif a=='phi':
      r = (self.x**2+self.y**2)**.5
      self.x = r*cos(v)
      self.y = r*sin(v)
    else:
      super().__setattr__(a,v)

  def __delattr__(self,a):
    if a in ['x','y']:
      raise AttributeError
    super().__delattr__(a)


w=Wektor(0,1)
print(w.r, w.phi)
w.phi=pi/4
print(w.x, w.y)
w.r=2
print(w.x, w.y)
w.y=1
print(w.r, w.phi)
del w.x
