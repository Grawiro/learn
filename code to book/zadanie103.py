import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
  
alfa=np.linspace(0,6.28,51)
beta=np.linspace(0,6.28,51)
  
alfa,beta=np.meshgrid(alfa,beta)
  
X=(100+60*np.cos(beta))*np.cos(alfa)
Y=(100+60*np.cos(beta))*np.sin(alfa)
Z=60* np.sin(beta)
  
fig = plt.figure()
ax = Axes3D(fig)
surf=ax.plot_surface(X, Y, Z, rstride=4, cstride=1, linewidth=0.1, alpha=0.5)
ax.auto_scale_xyz([-160, 160], [-160, 160], [-120, 120])
plt.show()
