class Wektor_h(Wektor):

  def __mul__(self,drugi):
    if isinstance(drugi,Wektor_h):
      return Wektor_h(self.x*drugi.x,self.y*drugi.y)
    else:
      return Wektor_h(drugi*self.x,drugi*self.y)

  def __rmul__(self,drugi):
    return Wektor_h(drugi*self.x,drugi*self.y)
