import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Julia set function
def julia(c, max_iter):
    def f(z):
        return z * z + c
    return f

# Generate Julia set image for a given region
def generate_julia_image(xmin, xmax, ymin, ymax, width, height, max_iter, c):
    image = np.zeros((height, width))
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)

    for ix in range(width):
        for iy in range(height):
            z = complex(x[ix], y[iy])
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z*z + c
                n += 1
            image[iy, ix] = n
    return image

# Create animation function
def animate(i, ax, width, height, max_iter, c):
    # Zoom into the Julia set more quickly
    scale = 2 ** (i * 0.2)  # Faster zoom by using a higher exponent
    xmin, xmax = -2 / scale, 2 / scale
    ymin, ymax = -2 / scale, 2 / scale

    image = generate_julia_image(xmin, xmax, ymin, ymax, width, height, max_iter, c)
    
    ax.clear()
    ax.imshow(image, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    ax.set_title(f'Julia Set Zoom: Iteration {i}')
    ax.axis('off')

# Set up the plot and animation
width, height = 800, 800
max_iter = 256
c = complex(-0.70176, -0.3842)  # A common Julia set constant

fig, ax = plt.subplots(figsize=(8, 8))

ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(ax, width, height, max_iter, c), interval=50)

plt.show()
