import numpy as np
from time import time
from multiprocessing import Process, Pipe


x=np.arange(-2,1.01,.001)
y=np.arange(-1.5,1.51,.001)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape


def mand(z,lewy_koniec):
  t=time()
  z0=np.copy(z)
  s=z.shape
  res=255*np.ones(s)
  for i in range(255):
    res[np.logical_and(np.abs(z)>2,res==255)]=i
    z=z**2+z0
  print(time()-t)
  lewy_koniec.send(res)


n=4
p=[Pipe() for i in range(n)]
l=[(z[:,i*s[1]//n:(i+1)*s[1]//n],p[i][0]) for i in range(n)] # lista krotek (obszar, lewy_koniec)
l=[Process(target=mand,args=i) for i in l]
for i in l:
  i.start()

import matplotlib.pyplot as plt
plt.imshow(np.hstack([pipe[1].recv() for pipe in p]))
plt.show()
