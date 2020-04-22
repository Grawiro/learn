import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x = np.arange(0, 2*np.pi, 0.01)
fig, ax = plt.subplots()
line = ax.plot(x, np.sin(x))[0]


def animate(i):
  line.set_ydata(np.sin(x + i/10.0))


a=FuncAnimation(fig, animate, np.arange(1, 25, 0.1), interval=25)
plt.show()
