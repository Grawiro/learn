from functools import wraps

def gradient(f):
  if callable(f):
    dx=1e-5
    @wraps(f)
    def nowa(*x):
      f0=f(*x)
      g=[]
      for i in range(len(x)):
        x1=list(x)
        x1[i]+=dx
        g.append((f(*x1) - f0)/dx)
      return g
    return nowa
  else:
    dx=f
    def d(f):
      @wraps(f)
      def nowa(*x):
        f0=f(*x)
        g=[]
        for i in range(len(x)):
          x1=list(x)
          x1[i]+=dx
          g.append((f(*x1) - f0)/dx)
        return g
      return nowa
    return d
  
@gradient
def f(x,y):
  return x**2+y**2

print(f(1,1))

@gradient(1e-1)
def f(x,y):
  return x**2+y**2

print(f(1,1))
