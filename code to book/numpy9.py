import numpy as np
import matplotlib.pyplot as plt


T=25*np.ones((100,100))
T[:,0]=T[:,-1]=0
T[0,:]=T[-1,:]=50

N=128 # liczba uśrednień
for i in range(N):
  T[1:-1,1:-1]=(T[2:,1:-1]+T[:-2,1:-1]+T[1:-1,2:]+T[1:-1,:-2])/4

plt.imshow(T)
plt.show()
