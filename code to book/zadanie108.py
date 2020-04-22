import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation


m1=1.5; m2=2   # [kg]
l1=1; l2=0.6   # [m]
g=9.81         # [m/s^2]

a=m1*l1**2/3+m2*l1**2
c=m2*l2**2/3
b=m2*l1*l2/2
p=(m1/2+m2)*g*l1
q=m2*g*l2/2


def pole(X,t=0):
  mianownik=a*c-(b*np.cos(X[1]-X[0]))**2
  dteta1 = X[2]
  dteta2 = X[3]
  z1=b*np.sin(X[0]-X[1])*X[3]**2+p*np.sin(X[0])
  z2=b*np.sin(X[1]-X[0])*X[2]**2+q*np.sin(X[1])
  domega1= -(c*z1-b*np.cos(X[0]-X[1])*z2)/mianownik
  domega2= -(a*z2-b*np.cos(X[1]-X[0])*z1)/mianownik
  return [dteta1, dteta2, domega1, domega2]


t=np.linspace(0,10,1001)
rozw=odeint(pole,[3*np.pi/4,3*np.pi/4,0,0],t)

fig, ax = plt.subplots()
tx=[100*l1*np.sin(rozw[0,0])+100*l2*np.sin(rozw[0,1])]
ty=[-100*l1*np.cos(rozw[0,0])-100*l2*np.cos(rozw[0,1])]
tr=ax.plot(tx,ty,color='g')[0]
pret1 = ax.plot([0,100*l1*np.sin(rozw[0,0])], [0,-100*l1*np.cos(rozw[0,0])],linewidth=2,color='r')[0]
pret2 = ax.plot([0,100*l1*np.sin(rozw[0,0])+100*l2*np.sin(rozw[0,1])], [0,-100*l1*np.cos(rozw[0,0])-100*l2*np.cos(rozw[0,1])],linewidth=2,color='r')[0]


def anim(i):
  pret1.set_xdata([0,100*l1*np.sin(rozw[i,0])])
  pret1.set_ydata([0,-100*l1*np.cos(rozw[i,0])])
  pret2.set_xdata([100*l1*np.sin(rozw[i,0]),100*l1*np.sin(rozw[i,0])+100*l2*np.sin(rozw[i,1])])
  pret2.set_ydata([-100*l1*np.cos(rozw[i,0]),-100*l1*np.cos(rozw[i,0])-100*l2*np.cos(rozw[i,1])])
  tx.append(100*l1*np.sin(rozw[i,0])+100*l2*np.sin(rozw[i,1]))
  ty.append(-100*l1*np.cos(rozw[i,0])-100*l2*np.cos(rozw[i,1]))
  tr.set_xdata(tx)
  tr.set_ydata(ty)

  
a = FuncAnimation(fig,anim,range(len(t)),interval=10,repeat=False)
ax.set_xlim([-240,240])
ax.set_ylim([-180,180])
plt.show()

