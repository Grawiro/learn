class Quaternion:

  def __init__(*args):
    if len(args)==2:
      if type(args[1]) == complex:
    args[0].r=args[1].real
    args[0].i=args[1].imag
    args[0].j=0.
    args[0].k=0.
      else:
    try:
      args[0].r=float(args[1])
      args[0].i=0.
      args[0].j=0.
      args[0].k=0.
    except:
      raise ValueError
    elif len(args)==5:
      try:
    args[0].r=float(args[1])
    args[0].i=float(args[2])
    args[0].j=float(args[3])
    args[0].k=float(args[4])
      except:
    raise ValueError
    else:
      raise ValueError
  
  def __add__(self,drugi):
    if not isinstance(drugi,Quaternion):
      drugi=Quaternion(drugi)
    return Quaternion(self.r+drugi.r,self.i+drugi.i,self.j+drugi.j,self.k+drugi.k)

  def __sub__(self,drugi):
    if not isinstance(drugi,Quaternion):
      drugi=Quaternion(drugi)
    return Quaternion(self.r-drugi.r,self.i-drugi.i,self.j-drugi.j,self.k-drugi.k)
  
  def __mul__(self,drugi):
    if not isinstance(drugi,Quaternion):
      drugi=Quaternion(drugi)
    return Quaternion(self.r*drugi.r-self.i*drugi.i-self.j*drugi.j-self.k*drugi.k,
            self.r*drugi.i+self.i*drugi.r+self.j*drugi.k-self.k*drugi.j,
            self.r*drugi.j+self.j*drugi.r+self.k*drugi.i-self.i*drugi.k,
            self.r*drugi.k+self.k*drugi.r+self.i*drugi.j-self.j*drugi.i)
  
  def conj(self):
    return Quaternion(self.r,-self.i,-self.j,-self.k)
  
  def __truediv__(self,drugi):
    if not isinstance(drugi,Quaternion):
      drugi=Quaternion(drugi)
    return self*drugi.conj()/(drugi*drugi.conj())
  
  def __truediv__(self,drugi):
    if not isinstance(drugi,Quaternion):
      drugi=Quaternion(drugi)
    l=self*drugi.conj()
    m=(drugi*drugi.conj()).r
    return Quaternion(l.r/m,l.i/m,l.j/m,l.k/m)
  
  __radd__=__add__
  
  def __rsub__(self,drugi):
    drugi=Quaternion(drugi)
    return drugi.__sub__(self)

  def __rmul__(self,drugi):
    drugi=Quaternion(drugi)
    return drugi.__mul__(self)

  def __rtruediv__(self,drugi):
    drugi=Quaternion(drugi)
    return drugi.__truediv__(self)
  
  def __str__(self):
    return str(self.r)+('+' if self.i>=0 else '-')+str(abs(self.i))+'i'+('+' if self.j>=0 else '-')+str(abs(self.j))+'j'+('+' if self.k>=0 else '-')+str(abs(self.k))+'k'
