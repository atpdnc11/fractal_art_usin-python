import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

r = np.sin(8 * phi) * np.cos(8 * theta)
X = r * np.sin(phi) * np.cos(theta)
Y = r * np.sin(phi) * np.sin(theta)
Z = r * np.cos(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='cyan')
plt.show()