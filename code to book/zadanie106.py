import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def LV(p,t):
  x,y=p
  return (x*(5-.005*x-.2*y),y*(-1+.03*x-.01*y))

t=np.arange(0,10,.01)
rozw=odeint(LV,[60,20],t)

plt.plot(t,rozw)
plt.show()
  
