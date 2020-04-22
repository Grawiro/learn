import numpy as np
from time import time
from multiprocessing import Process, Array


x=np.arange(-2,1.01,.001)
y=np.arange(-1.5,1.51,.001)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape


def mand(z,res,l,p):
  t=time()
  z0=np.copy(z)
  s=z.shape
  res_local=255*np.ones(s)
  for i in range(255):
    res_local[np.logical_and(np.abs(z)>2,res_local==255)]=i
    z=z**2+z0
  print(time()-t)
  res[s[1]*l:s[1]*p]=res_local.flatten()


n=4
res=Array('d',np.zeros(s).flatten(5))
l=[(z[i*s[0]//n:(i+1)*s[0]//n,:], res, i*s[1]//n, (i+1)*s[1]//n) for i in range(n)]

l=[Process(target=mand,args=i) for i in l]
for i in l:
  i.start()
for i in l:
  i.join()

import matplotlib.pyplot as plt
plt.imshow(np.array(res).reshape(s))
plt.show()
