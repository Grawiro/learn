import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.random import rand, randn


lo=-8;  up=8;   S=1000;
k=.1;   a=.9;   b=.04;  c=.06


def f(x,y):
  obszar=np.logical_or(np.logical_or(x<lo,x>up),np.logical_or(y<lo,y>up))
  return (2*np.cos(x+y)**2/(1+(x-y)**2/10)+np.sin(x-y)**3+0.5*np.sin(.6*x+y))*(1-obszar) + 1*obszar


x=lo+(up-lo)*rand(2,S)
p=np.copy(x)
v=k*(up-lo)*randn(2,S)

X,Y=np.meshgrid(np.linspace(lo,up,1000),np.linspace(lo,up,1000))
fig,ax = plt.subplots(figsize=(12, 12), dpi=80)
ax.contourf(X,Y,f(X,Y),100)
line = ax.plot(x[0],x[1],'.k')[0]


def step():
  global g,v,x,p
    i=np.argmin(f(*p))                          # POPRAWKA KODU W KSIĄŻCE! Globalne minimum jest brane z lokalnych minimów, nie aktualnych położeń
  g=p[:,i:i+1]                                  # POPRAWKA KODU W KSIĄŻCE! p zamiast x
  v=a*v+b*rand(1,S)*(p-x)+c*rand(1,S)*(g-x)     # POPRAWKA KODU W KSIĄŻCE! Obie składowe wektora b mnożone są przez tę samą liczbę pseudolosową, podobnie dla wektora c!
  x+=v
  p=np.array(list(zip(*[min(j,key=lambda i:f(*i)) for j in zip(p.T,x.T)])))


def animate(i):
  step()
  line.set_xdata(np.array(x[0]))
  line.set_ydata(np.array(x[1]))


fa=FuncAnimation(fig,animate,range(200),interval=200,repeat=False)
plt.show()
