import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-1.5,1.5,31)
plt.plot(X,X**2,label='f.kwadratowa',color='g',linewidth=2,marker='*',markersize=10,markerfacecolor='y')
plt.plot(X,X**3,label='f.szescienna',color='b',linewidth=2,marker='o',markersize=10,markerfacecolor='r')
plt.legend()
plt.show()
