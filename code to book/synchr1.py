import numpy as np
import matplotlib.pyplot as plt


N=200
T=25*np.ones((N,N))
dx=1./N             # [m]
T[:,0]=T[:,-1]=0    # [C]
T[0,:]=T[-1,:]=50   # [C]
k = 5.8e-2          # [W/K]
Q=np.zeros((N,N))
for j in range(N//4,3*N//4):
  Q[int(N/2+N/10*np.sin(20.*(j-N/2)/N)),j]=5e3*dx**2        # [W]

emin=1e-3
imax=60000

i=0
while True:
  T0=np.copy(T)
  T[1:-1,1:-1]=(T[2:,1:-1]+T[:-2,1:-1]+T[1:-1,2:]+T[1:-1,:-2] + Q[1:-1,1:-1]/k)/4
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
