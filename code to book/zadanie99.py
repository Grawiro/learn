import numpy as np
import matplotlib.pyplot as plt


X = np.linspace(0,1,101)

for a in np.linspace(.25,2,8):
  plt.plot(X,X**a,color=(a/2,0,1-a/2),label='$x^{%s}$' % a)
plt.legend()
plt.show()
