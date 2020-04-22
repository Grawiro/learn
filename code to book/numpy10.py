import numpy as np
import matplotlib.pyplot as plt


T=25*np.ones((100,100))
T[:,0]=T[:,-1]=0
T[0,:]=T[-1,:]=50

emin=.001
imax=2048
i=0
while True:
  T0=np.copy(T)
  T[1:-1,1:-1]=(T[2:,1:-1]+T[:-2,1:-1]+T[1:-1,2:]+T[1:-1,:-2])/4
  i+=1
  if i > imax:
    print('Osiągnięto maksymalną liczba iteracji, dokładność:', e)
    break
  e=np.max(abs(T-T0))
  if e < emin:
    print('Osiągnięto pożądaną dokładność, liczba iteracji:', i)
    break

plt.imshow(T)
plt.show()
