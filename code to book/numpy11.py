#coding=utf8
import numpy as np
import matplotlib.pyplot as plt


T=25*np.ones((100,100))
T[:,0]=T[:,-1]=0
T[0,:]=T[-1,:]=50

Q = np.zeros((100,100))
Q[30,30] = 2                # [W]
Q[70,70] = -3               # [W]
k = 5.8e-2                  # [W/K]

emin=.001
imax=4096
i=0
while True:
  T0=np.copy(T)
  T[1:-1,1:-1]=(T[2:,1:-1]+T[:-2,1:-1]+T[1:-1,2:]+T[1:-1,:-2]+Q[1:-1,1:-1]/k)/4
  i+=1
  if i > imax:
    print('Osiągnięto maksymalną ilość iteracji, dokładność:', e)
    break
  e=np.max(abs(T-T0))
  if e < emin:
    print('Osiągnięto pożądaną dokładność, ilość iteracji:', i)
    break

plt.imshow(T)
plt.show()
