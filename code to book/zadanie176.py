import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Pipe, Queue


X = np.linspace(-1,1,1000); dx = 2./1000
V=np.zeros(X.shape);V[abs(X)<.05] = 5e3
Psi = np.exp(-1024*(X-.5)**2)*np.exp(-64j*X)
Psi /= np.sum(np.abs(Psi**2)*dx)**.5

plt.plot(X,np.abs(Psi)**2)


def proces(Psi,V,pl,pp,q,num):
  hbar = 1e0; m = 1e0; e = 1e0; dt = 5e-8
  def H(Psi):
    return  - hbar**2/(2*m) * (np.concatenate((Psi[1:],r))+np.concatenate((l,Psi[:-1]))-2*Psi)/dx**2 + e * V * Psi
  def RK4(Psi):
    k1 = H(Psi)/(1j*hbar)*dt
    k2 = H(Psi+k1/2)/(1j*hbar)*dt
    k3 = H(Psi+k2/2)/(1j*hbar)*dt
    k4 = H(Psi+k3)/(1j*hbar)*dt
    return (k1+2*k2+2*k3+k4)/6
  for i in range(128000):
    pl.send(Psi[:1])
    pp.send(Psi[-1:])
    l=pl.recv()
    r=pp.recv()
    Psi+=RK4(Psi)
  q.put((num,Psi))


class PseudoConnection:

  def __init__(self,x):
    self.x=x

  send = lambda self,y:None
  recv = lambda self:self.x


n=2             # liczba podprocesow
N=Psi.shape[0]  # liczba punktow siatki obliczeniowej
pi=[PseudoConnection(Psi[:1])]+sum([list(Pipe()) for i in range(n-1)],[])+[PseudoConnection(Psi[-1:])]
q=Queue()
pr=[Process(target=proces,args=(Psi[1+i*(N-2)//n:1+(i+1)*(N-2)//n],V[1+i*(N-2)//n:1+(i+1)*(N-2)//n],pi[2*i],pi[2*i+1],q,i)) for i in range(n)]

for p in pr:
  p.start()
l=sorted([q.get() for j in range(n)],key=lambda i:i[0])

Psi=np.concatenate([Psi[:1]]+[i[1] for i in l]+[Psi[-1:]])
plt.plot(X,np.abs(Psi)**2)
plt.plot(X,10*V/np.max(V))
plt.show()
