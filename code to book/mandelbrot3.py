import numpy as np
x=np.arange(-2,1.01,.01)
y=np.arange(-1.5,1.51,.01)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
    
fig = plt.figure(figsize=(12,9))

z0=np.copy(z)
res=255*np.ones(s)
w=plt.imshow(res,vmin=0,vmax=255)

def anim(i):
  global z
  res[np.logical_and(np.abs(z)>2,res==255)]=i
  z=(res==255)*(z**2+z0)
  w.set_array(res)

a=FuncAnimation(fig,anim,frames=256,interval=40,repeat=False)
plt.show()
