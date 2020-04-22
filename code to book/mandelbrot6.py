import numpy as np
from time import time
from multiprocessing import Process

x=np.arange(-2,1.01,.001)
y=np.arange(-1.5,1.51,.001)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape


def mand(z):
  t=time()
  z0=np.copy(z)
  s=z.shape
  res=255*np.ones(s)
  for i in range(255):
    res[np.logical_and(np.abs(z)>2,res==255)]=i
    z=(z**2+z0)
  print('funkcja: ', time()-t)


t=time()
n=4
l=[z[:,i*s[1]//n:(i+1)*s[1]//n] for i in range(n)]
l=[Process(target=mand,args=(i,)) for i in l]
t=time()
for i in l:
  i.start()
for i in l:
  i.join()
print('program: ', time()-t)
