from functools import wraps

def pochodna(f):
  if callable(f):
    dx=1e-5
    @wraps(f)
    def nowa(x):
      return (f(x+dx)-f(x))/dx
    return nowa
  else:
    dx=f
    def d(f):
      @wraps(f)
      def nowa(x):
        return (f(x+dx)-f(x))/dx
      return nowa
    return d

