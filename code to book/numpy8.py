import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

fi=np.linspace(-3.14,3.14,21)
om=np.linspace(-2,2,21)
fi,om=np.meshgrid(fi,om)

def pole(punkt,t=0):
  return (punkt[1],-np.sin(punkt[0]))

t=np.linspace(0,50,5001)
rozw=odeint(pole,[3,0],t)

fig, ax = plt.subplots()
pret = ax.plot([0,100*np.sin(3)], [0,-100*np.cos(3)])[0]
kulka = ax.plot([100*np.sin(3)],[-100*np.cos(3)],'o')[0]

def anim(i):
  pret.set_xdata([0,100*np.sin(rozw[i,0])])
  pret.set_ydata([0,-100*np.cos(rozw[i,0])])
  kulka.set_xdata([100*np.sin(rozw[i,0])])
  kulka.set_ydata([-100*np.cos(rozw[i,0])])

a = FuncAnimation(fig,anim,range(len(rozw)),interval=10)
ax.set_xlim([-200,200])
ax.set_ylim([-150,150])
plt.show()
