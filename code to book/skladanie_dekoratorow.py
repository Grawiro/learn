from functools import wraps
import numpy as np
import matplotlib.pyplot as plt


def dekorator(f):
  def wew(x):
    y=f(x)
    if y<-1:
      y=-1
    elif y>1:
      y=1
    return y
  return wew

  
def pochodna(f):
  dx=1e-5
  @wraps(f)
  def nowa(x):
    return (f(x+dx)-f(x))/dx
  return nowa

  
@dekorator
@pochodna
def f1(x):
  return x**2


@pochodna
@dekorator
def f2(x):
  return x**2


X=np.linspace(-2,2,401)
plt.plot(X,map(f1,X))
plt.plot(X,map(f2,X))
plt.show()
