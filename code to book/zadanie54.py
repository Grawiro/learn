# Kod uzupełniający ciało klasy Ulamek

  def __gt__(self,drugi):
    if isinstance(drugi,Ulamek):
      return (self.l*drugi.m-drugi.l*self.m)*(self.m*drugi.m) > 0
    else:
      return(self.l-drugi*self.m)*self.m > 0

  def __ge__(self,drugi):
    if isinstance(drugi,Ulamek):
      return (self.l*drugi.m-drugi.l*self.m)*(self.m*drugi.m) >= 0
    else:
      return(self.l-drugi*self.m)*self.m >= 0

  def __lt__(self,drugi):
    if isinstance(drugi,Ulamek):
      return (self.l*drugi.m-drugi.l*self.m)*(self.m*drugi.m) < 0
    else:
      return(self.l-drugi*self.m)*self.m < 0

  def __le__(self,drugi):
    if isinstance(drugi,Ulamek):
      return (self.l*drugi.m-drugi.l*self.m)*(self.m*drugi.m) <= 0
    else:
      return(self.l-drugi*self.m)*self.m <= 0

  def __eq__(self,drugi):
    if isinstance(drugi,Ulamek):
      return self.l*drugi.m == drugi.l*self.m
    else:
      return self.l == drugi*self.m

  def __ne__(self,drugi):
    if isinstance(drugi,Ulamek):
      return self.l*drugi.m != drugi.l*self.m
    else:
      return self.l != drugi*self.m
  
