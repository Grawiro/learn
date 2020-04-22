from functools import wraps

def dekorator(*args):
  if callable(args[0]):
    a=-1
    b=1
    f=args[0]
    @wraps(f)
    def wew(x):
      y=f(x)
      if y<a:
        y=a
      elif y>b:
        y=b
      return y
    return wew
  else:
    if len(args)==2:
      a,b=args
    else:
      a=-args[0]
      b=args[0]
    def d(f):
      @wraps(f)
      def wew(x):
        y=f(x)
        if y<a:
          y=a
        elif y>b:
          y=b
        return y
      return wew
    return d
  
@dekorator(1,2)
def f1(x):
  return 2*x
  
@dekorator(2)
def f2(x):
  return 2*x
  
@dekorator
def f3(x):
  return 2*x

print(f1(-1.5), f2(-1.5), f3(-1.5))
