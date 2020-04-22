import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X,Y=np.meshgrid(np.linspace(-1.57,1.57,100),np.linspace(-1.57,1.57,100))
Z=np.sin(2*X)+1.5*np.cos(Y)**4+2*np.cos(X+Y)
plt.contour(X,Y,Z,50)
X=X[::5,::5]
Y=Y[::5,::5]
VX=2*np.cos(2*X)-2*np.sin(X+Y)
VY=-6*np.cos(Y)**3*np.sin(Y)-2*np.sin(X+Y)
plt.quiver(X,Y,VX,VY)
plt.show()
