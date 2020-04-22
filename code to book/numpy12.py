#coding=utf8
import numpy as np
import matplotlib.pyplot as plt


T = np.zeros((400,400))
x,y=np.meshgrid(np.arange(-200,200),np.arange(-200,200))
T[abs(x)<abs(y)]=50
T[x**2+y**2>180**2]=np.NaN
T[x**2+y**2<175**2]=25

Q = np.zeros((400,400))
k = 5.8e-2                # [W/K]

emin=.001
imax=10000
i=0
while True:
  T0=np.copy(T)
  X=(T[2:,1:-1]+T[:-2,1:-1]+T[1:-1,2:]+T[1:-1,:-2]+Q[1:-1,1:-1]/k)/4
  T[1:-1,1:-1]=np.isnan(X)*T[1:-1,1:-1]
  X[np.isnan(X)]=0
  T[1:-1,1:-1]+=X   
  i+=1
  if i > imax:
    print('Osiągnięto maksymalną ilość iteracji, dokładność:', e)
    break
  e=np.max(abs((T-T0)[np.logical_not(np.isnan(T))]))
  if e < emin:
    print('Osiągnięto pożądaną dokładność, ilość iteracji:', i)
    break

plt.imshow(T)
plt.show()
