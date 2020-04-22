def f(z):
  z0=z
  for i in range(255):
    if abs(z)>2:
      return i
    z=z**2+z0
  return 255
  
import numpy as np
x=np.arange(-2,1.01,.01)
y=np.arange(-1.5,1.51,.01)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape

from time import time
t=time()
z0=np.copy(z)
res=255*np.ones(s)
for i in range(255):
  res[np.logical_and(np.abs(z)>2,res==255)]=i
  z=z**2+z0
print(time()-t)

import matplotlib.pyplot as plt
plt.imshow(res)
plt.show()
