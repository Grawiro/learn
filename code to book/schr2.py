import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-1,1,1000); dx = 2./1000
V=np.zeros(X.shape);V[abs(X)<.05] = 5e3
Psi = np.exp(-1024*(X-.5)**2)*np.exp(-64j*X)
Psi /= np.sum(np.abs(Psi**2))**.5

plt.plot(X,np.abs(Psi)**2)

hbar = 1e0; m = 1e0; e = 1e0; dt = 5e-8

def H(Psi):
  return  - hbar**2/(2*m) * (np.concatenate((Psi[1:],[0]))+np.concatenate(([0],Psi[:-1]))-2*Psi)/dx**2 + e * V * Psi

def RK4(Psi):
  k1 = H(Psi)/(1j*hbar)*dt
  k2 = H(Psi+k1/2)/(1j*hbar)*dt
  k3 = H(Psi+k2/2)/(1j*hbar)*dt
  k4 = H(Psi+k3)/(1j*hbar)*dt
  return (k1+2*k2+2*k3+k4)/6

for j in range(128000):
  Psi += RK4(Psi)

plt.plot(X,np.abs(Psi)**2)
plt.plot(X,.015*V/np.max(V))
plt.show()
