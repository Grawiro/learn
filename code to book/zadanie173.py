import numpy as np
from time import time
from multiprocessing import Process, Queue


x=np.arange(-2,1.01,.001) #x=np.linspace(-2,1.001,.001)
y=np.arange(-1.5,1.51,.001)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape


def mand(z,q,num):
  t=time()
  z0=np.copy(z)
  s=z.shape
  res=255*np.ones(s)
  for i in range(255):
    res[np.logical_and(np.abs(z)>2,res==255)]=i
    z=(z**2+z0)
  print('funkcja ',num,': ', time()-t)
  q.put((num,res))


t=time()
n=4
l=[z[:,i*s[1]/n:(i+1)*s[1]/n] for i in range(n)]
q=Queue()
l=[Process(target=mand,args=(z[:,i*s[1]/n:(i+1)*s[1]/n],q,i)) for i in range(n)]
t=time()
for i in l:
  i.start()
res=[q.get() for i in range(n)]
res.sort()
res=map(lambda i:i[1],res)
res=np.hstack(res)
print('program: ', time()-t)

import matplotlib.pyplot as plt
plt.imshow(res)
plt.show()

