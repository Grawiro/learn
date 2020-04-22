class Wektor:

  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __add__(self,drugi):
    return Wektor(self.x+drugi.x,self.y+drugi.y)

  def __sub__(self,drugi):
    return Wektor(self.x-drugi.x,self.y-drugi.y)
    # ...
