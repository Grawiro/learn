import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process, Pipe, Queue


T=np.zeros((100,100))
T[:,0]=T[:,-1]=0
T[0,:]=T[-1,:]=50

N=200
T=25*np.ones((N,N))
dx=1./N             # [m]
T[:,0]=T[:,-1]=0    # [C]
T[0,:]=T[-1,:]=50   # [C]
k = 5.8e-2          # [W/K]
Q=np.zeros((N,N))
for j in range(N//4,3*N//4):
  Q[int(N/2+N/10*np.sin(20.*(j-N/2)/N)),j]=5e3*dx**2    # [W]

imax=60000

def proces_lewy(T,Q,p,q):
  for i in range(imax):
    p.send(T[1:-1,-1:]) # wysyłamy swój prawy brzeg
    kolumna=p.recv()    # odbieramy lewy brzeg sąsiada z prawej
    T[1:-1,1:]=(T[2:,1:]+T[:-2,1:]+np.hstack((T[1:-1,2:],kolumna))+T[1:-1,:-1] + Q[1:-1,1:]/k)/4
  q.put((0,T))

def proces_prawy(T,Q,p,q):
  for i in range(imax):
    p.send(T[1:-1,:1])  # wysyłamy swój lewy brzeg
    kolumna=p.recv()    # odbieramy prawy brzeg sąsiada z lewej
    T[1:-1,:-1]=(T[2:,:-1]+T[:-2,:-1]+T[1:-1,1:]+np.hstack((kolumna,T[1:-1,:-2])) + Q[1:-1,:-1]/k)/4
  q.put((1,T))

p=Pipe()
q=Queue()
pl=Process(target=proces_lewy,args=(T[:,:N//2],Q[:,:N//2],p[0],q))
pp=Process(target=proces_prawy,args=(T[:,N//2:],Q[:,N//2:],p[1],q))
pl.start()
pp.start()
l=sorted([q.get() for j in range(2)],key=lambda i:i[0])

plt.imshow(np.hstack([i[1] for i in l]))
plt.show()
