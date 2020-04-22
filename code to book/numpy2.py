import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-3,3,601)
Y=1/(X**2-1)
Y[abs(Y)>5]=np.NaN
label=r'$y=\frac{1}{x^2-1}$'
plt.plot(X,Y,label=label)
plt.plot([-1,-1],[-5,5],'--')
plt.plot([1,1],[-5,5],'--')
plt.legend()
plt.show()
