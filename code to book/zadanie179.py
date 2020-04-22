import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Queue, Process, Pipe
from time import time


def Laplasjan(T,dx):
  return (T[1:-1,2:]+T[1:-1,:-2]+T[2:,1:-1]+T[:-2,1:-1]-4*T[1:-1,1:-1])/dx**2


spf = 50   # krokow na klatke
N=200
dx=1./N
dt=dx**2/4 # stabilnosc metody!
T=25*np.ones((N,N))
T[0,:]=50       # [C]
T[-1,:]=0       # [C]
k = 5.8e-2      # [W/K]
Q=np.zeros((N,N))
for j in range(N//4,3*N//4):
  Q[int(N/2+N/10*np.sin(20.*(j-N/2)/N)),j]=4e3*dx**2 # [W]

max_iter=60000


def proces(T,Q,pL,pP,pK):
  for i in range(max_iter//spf):
    for j in range(spf):
      pL.send(T[:,:1])
      pP.send(T[:,-1:])
      kL=pL.recv()
      kP=pP.recv()
      T[1:-1,:]+=(Laplasjan(np.hstack((kL,T,kP)),dx)+Q[1:-1,:]/dx**2/k)*dt
    pK.send(T)


def kolekcjoner(lista_koncow,q):
  for i in range(max_iter//spf):
    q.put(np.hstack([koniec.recv() for koniec in lista_koncow]))


n=3
q=Queue()
konce=sum([list(Pipe()) for i in range(n)],[])
konce=[konce[-1]]+konce[:-1]
Kpi=[Pipe() for i in range(n)]
procesy=[Process(target=proces,args=(
  T[:,1+i*(N-2)//n:1+(i+1)*(N-2)//n],
  Q[:,1+i*(N-2)//n:1+(i+1)*(N-2)//n],
  konce[2*i], konce[2*i+1], Kpi[i][0]
  )) for i in range(n)]
for i in procesy:
  i.start()
Process(target=kolekcjoner,args=([p[1] for p in Kpi],q)).start()

fig = plt.figure(figsize=(12,9))
w=plt.imshow(T,vmin=0,vmax=78)

def anim(i):
  t=time()
  w.set_array(q.get())
  print(i,time()-t)

a=FuncAnimation(fig,anim,interval=20,frames=max_iter//spf-1,repeat=False)
plt.show()
