import numpy as np
from numpy.random import rand, randn
from time import time


k=.1;   a=.9;   b=.04;  c=.06
lo=-8;  up=8;   S=1000; maxiter=200


class NewMinimum(Exception):
  pass


def f(x,y):
  obszar=np.logical_or(np.logical_or(x<lo,x>up),np.logical_or(y<lo,y>up))
  return (2*np.cos(x+y)**2/(1+(x-y)**2/10)+np.sin(x-y)**3+0.5*np.sin(.6*x+y))*(1-obszar) + 1*obszar


def particle(x,v):
  global list_p
  p=np.copy(x)
  g=np.copy(x)
  fmin=f(*p)
  while True:
    try:
      yield
    except NewMinimum as e:
      g = e.args[0]
    except GeneratorExit:
      break
    v=a*v+b*rand(2)*(p-x)+c*rand(2)*(g-x)
    x+=v
    if f(*x)<fmin:
      p=np.copy(x)
      fmin=f(*p)
      if fmin<f(*g):
        list_p.append(p)


t=time()

swarm=[particle(lo+(up-lo)*rand(2),k*(up-lo)*rand(2)) for i in range(S)]
for i in swarm:
  i.send(None)

g=np.zeros(2)
for i in range(maxiter):
  list_p=[]
  for i in swarm:
    next(i)
  if list_p:
    g=min(list_p,key=lambda x:f(*x))
    for i in swarm:
      i.throw(NewMinimum(g))

print(g, f(*g))
print(time()-t)
