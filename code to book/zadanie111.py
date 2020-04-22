from time import time
import numpy as np

X,Y=np.meshgrid(np.linspace(-2,2,1001),np.linspace(-2,2,1001))
f=np.exp(-(X**2+Y**2)/2)

t=time()
L=(f[2:,1:-1]+f[:-2,1:-1]+f[1:-1,2:]+f[1:-1,:-2]-4*f[1:-1,1:-1])/.04**2
print(time()-t)

t=time()
L=np.array([[(f[i,j-1]+f[i,j+1]+f[i-1,j]+f[i+1,j]-4*f[i,j])/.04**2 for i in range(1,1000)] for j in range(1,1000)])
print(time()-t)
  
