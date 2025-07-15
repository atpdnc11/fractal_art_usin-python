import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, zoom=1, x_offset=0, y_offset=0):
    x = np.linspace(-2.5, 1.5, w) / zoom + x_offset
    y = np.linspace(-2, 2, h) / zoom + y_offset
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    output = np.zeros(C.shape, dtype=int)
    for i in range(256):
        Z = Z ** 2 + C
        mask = (np.abs(Z) > 2) & (output == 0)
        output[mask] = i
    return output

plt.imshow(mandelbrot(800, 800), cmap='inferno')
plt.axis('off')
plt.show()