import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pole(punkt,t=0):
  return (punkt[1],-np.sin(punkt[0]))

t=np.linspace(0,50,5001)
rozw=odeint(pole,[3,0],t)
plt.plot(t,rozw[:,0])
plt.plot(t,rozw[:,1])
plt.show()
