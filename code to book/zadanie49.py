class Wielomian(list):

  def __add__(self,drugi):
    ls=len(self)
    ld=len(drugi)
    if ls<=ld:
      return Wielomian([self[i]+drugi[i] for i in range(ls)]+drugi[ls:])
    else:
      return Wielomian([self[i]+drugi[i] for i in range(ld)]+self[ld:])

  def __sub__(self,drugi):
    ls=len(self)
    ld=len(drugi)
    if ls<=ld:
      return Wielomian([self[i]-drugi[i] for i in range(ls)]+[-i for i in drugi[ls:]])
    else:
      return Wielomian([self[i]-drugi[i] for i in range(ld)]+self[ld:])

  def __mul__(self,drugi):
    if isinstance(drugi,Wielomian):
      s=list(self)
      d=list(drugi)
      ls=len(s)-1
      ld=len(d)-1
      s+=[0]*ld
      d+=[0]*ls
      return Wielomian([sum(map(lambda i:i[0]*i[1],zip(s[:i+1],d[:i+1][::-1]))) for i in range(ls+ld+1)])
    else:
      return Wielomian([drugi*i for i in self])
      
  __rmul__ = __mul__

  def __pow__(self,exp):
    res=Wielomian([1])
    kw=self
    while exp:
      if exp%2:
        res*=kw
      kw*=kw
      exp/=2
    return res

  def __call__(self,x):
    return reduce(lambda a,b:x*a+b,self[::-1])
