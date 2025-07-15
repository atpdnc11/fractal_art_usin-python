import numpy as np
import matplotlib.pyplot as plt

def perlin(size, scale=10):
    def fade(t):
        return 6 * t**5 - 15 * t**4 + 10 * t**3

    # Grid of points
    lin = np.linspace(0, scale, size, endpoint=False)
    x, y = np.meshgrid(lin, lin)

    # Grid coordinates for gradient selection
    x0 = (x.astype(int)) % scale
    x1 = (x0 + 1) % scale
    y0 = (y.astype(int)) % scale
    y1 = (y0 + 1) % scale

    # Relative position inside the cell
    xf = x - x.astype(int)
    yf = y - y.astype(int)

    # Generate random gradient vectors
    angles = 2 * np.pi * np.random.rand(scale + 1, scale + 1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))

    # Fetch gradients at corner points
    g00 = gradients[x0, y0]
    g10 = gradients[x1, y0]
    g01 = gradients[x0, y1]
    g11 = gradients[x1, y1]

    # Vectors from grid points to input point
    d00 = np.dstack((xf, yf))
    d10 = np.dstack((xf - 1, yf))
    d01 = np.dstack((xf, yf - 1))
    d11 = np.dstack((xf - 1, yf - 1))

    # Compute dot products
    n00 = np.sum(g00 * d00, axis=2)
    n10 = np.sum(g10 * d10, axis=2)
    n01 = np.sum(g01 * d01, axis=2)
    n11 = np.sum(g11 * d11, axis=2)

    # Interpolate
    u = fade(xf)
    v = fade(yf)
    nx0 = n00 * (1 - u) + n10 * u
    nx1 = n01 * (1 - u) + n11 * u
    nxy = nx0 * (1 - v) + nx1 * v

    return nxy

# Display the Perlin noise
plt.figure(figsize=(6, 6))
plt.imshow(perlin(500, 8), cmap='gray', origin='upper')
plt.axis('off')
plt.show()
