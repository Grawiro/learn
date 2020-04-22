class Wektor_v(Wektor):

  def __mul__(self,drugi):
    if isinstance(drugi,Wektor_v):
      return self.x*drugi.y-self.y*drugi.x
    else:
      return Wektor_v(drugi*self.x,drugi*self.y)

  def __rmul__(self,drugi):
    return Wektor_v(drugi*self.x,drugi*self.y)
