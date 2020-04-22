import numpy as np
from time import time
from multiprocessing import Pool


x=np.arange(-2,1.002,.002)
y=np.arange(-1.5,1.502,.002)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape


def mand(z):
  z0=np.copy(z)
  s=z.shape
  res=255*np.ones(s)
  for i in range(255):
    res[np.logical_and(np.abs(z)>2,res==255)]=i
    z=(z**2+z0)
  return res


p = Pool()

t=time()
n=4
l=[z[:,i*s[1]//n:(i+1)*s[1]//n] for i in range(n)]
l=p.map(mand,l)
res=np.hstack(l)
print(time()-t)

import matplotlib.pyplot as plt
plt.imshow(res)
plt.show()
