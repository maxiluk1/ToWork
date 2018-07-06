from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-10, 10)
Y = np.arange(-10, 10)

X, Y = np.meshgrid(X, Y)

Z = (np.cos(X)/np.sin(X))**2+(np.sin(Y)/np.cos(Y))*X

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

ax.set_xlabel("x")
ax.set_ylabel("y")

plt.axis([-10,10,-10,10])

plt.title("Zad_1b")
plt.show()