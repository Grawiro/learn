import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pole(punkt,t=0):
  return (punkt[1],-np.sin(punkt[0]))

fi=np.linspace(-3.14,3.14,21)
om=np.linspace(-2,2,21)
fi,om=np.meshgrid(fi,om)

dfi,dom=pole((fi,om))
plt.quiver(fi,om,dfi,dom,width=0.002,scale=40)
t=np.linspace(0,15,1501)
for phi0 in np.linspace(.1,3.1,16):
  rozw = odeint(pole,[phi0,0],t)
  plt.plot(rozw[:,0],rozw [: ,1],'b')
plt.show()
