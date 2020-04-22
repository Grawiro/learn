import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


X = np.linspace(-1,1,1000); dx = 2./1000
V=np.zeros(X.shape);V[abs(X)<.05] = 5e3
Psi = np.exp(-1024*(X-.5)**2)*np.exp(-64j*X)
Psi /= np.sum(np.abs(Psi**2)*dx)**.5

hbar = 1e0
m = 1e0
e = 1e0
dt = 1e-8


def H(Psi):
  return  - hbar**2/(2*m) * (Psi[2:]+Psi[:-2]-2*Psi[1:-1])/dx**2 + e * V[1:-1] * Psi[1:-1]

  
fig, ax = plt.subplots()
w=plt.plot(X,Psi)
ax.set_ylim((0,10))
plt.plot(X,10*V/np.max(V))


def anim(i):
  global Psi
  for j in range(5000):
    Psi[1:-1] += H(Psi)*dt/(1j*hbar)
  w[0].set_ydata(np.abs(Psi**2))
  print(i)
  return w

  
a=FuncAnimation(fig,anim,frames=512,interval=20,repeat=False)
plt.show()
