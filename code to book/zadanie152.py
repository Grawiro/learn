def typowanie(warunek):
  def dekorator(f):
    def nowa(*args):
      if warunek(tuple(map(type,args))):
        return f(*args)
      else:
        raise TypeError
    return nowa
  return dekorator
  
  
@typowanie(lambda x:all([i in (int,float) for i in x]))
def funkcja(x,y):
  return x**2+y**2
  
  
print(funkcja(1,2.0))
print(funkcja(1j,1j))
