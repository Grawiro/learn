class Permutation:

  def __init__(self,l):
    if all([i in l for i in range(len(l))]):
      self.l=l
    else:
      raise ValueError('Elementami listy powinny być wartości permutacji na kolejnych elementach ciągu {0, ..., n-1}')

  def __mul__(self,druga):
    if len(self.l) != len(druga.l):
      raise ValueError('Permutacje powinny być tej samej długości')
    return Permutation([self.l[i] for i in druga.l])
  
  def __pow__(self,exp):
    res=Permutation(range(len(self.l)))
    kw=self
    while exp:
      if exp%2:
        res*=kw
      kw*=kw
      exp/=2
    return res

  def __neg__(self):
    return Permutation(map(self.l.index, range(len(self.l))))

  def __call__(self,l):
    if len(self.l) != len(l):
      raise ValueError('Permutacja powinna mieć tę samą długość co lista')
    return [l[self.l.index(i)] for i in range(len(self.l))]

  def __str__(self):
    return str(self.l)
