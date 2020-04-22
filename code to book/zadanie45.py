class Wektor_s(Wektor):

  def __mul__(self,drugi):
    if isinstance(drugi,Wektor):
      return self.x*drugi.x+self.y*drugi.y
    else:
      return Wektor_s(drugi*self.x,drugi*self.y)

  def __rmul__(self,drugi):
    return Wektor_s(drugi*self.x,drugi*self.y)
