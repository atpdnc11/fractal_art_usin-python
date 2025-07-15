import numpy as np
import matplotlib.pyplot as plt

def perlin(size, scale=10):
    def f(t): return 6*t**5 - 15*t**4 + 10*t**3
    lin = np.linspace(0, scale, size, endpoint=False)
    x, y = np.meshgrid(lin, lin)
    angles = 2*np.pi*np.random.rand(scale+1, scale+1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    g00 = gradients[:-1,:-1]
    g10 = gradients[1:,:-1]
    g01 = gradients[:-1,1:]
    g11 = gradients[1:,1:]
    n00 = (x-x.astype(int))*g00[:,:,0] + (y-y.astype(int))*g00[:,:,1]
    n10 = (x-x.astype(int)-1)*g10[:,:,0] + (y-y.astype(int))*g10[:,:,1]
    n01 = (x-x.astype(int))*g01[:,:,0] + (y-y.astype(int)-1)*g01[:,:,1]
    n11 = (x-x.astype(int)-1)*g11[:,:,0] + (y-y.astype(int)-1)*g11[:,:,1]
    tx, ty = f(x-x.astype(int)), f(y-y.astype(int))
    nx0 = n00*(1-tx) + n10*tx
    nx1 = n01*(1-tx) + n11*tx
    nxy = nx0*(1-ty) + nx1*ty
    return nxy

plt.imshow(perlin(500), cmap='gray')
plt.axis('off')
plt.show()