# Kod uzupełniający ciało klasy Wielomian

  def dzielenie(self,dzielnik):
    res=[]
    reszta=Wielomian(self)
    ld=len(dzielnik)
    odwr_najw=1/dzielnik[-1]
    dzielnik=dzielnik[:-1]
    for i in range(len(self)-ld+1,0,-1):
      x=1.0*reszta.pop()*odwr_najw
      res.append(x)
      reszta-=Wielomian([0]*(i-ld+1)+dzielnik)*x
    return res[::-1], reszta

  def __floordiv__(self,drugi):
    return self.dzielenie(drugi)[0]
    
  def __mod__(self,drugi):
    return self.dzielenie(drugi)[1]
