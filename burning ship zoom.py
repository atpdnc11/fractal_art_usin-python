import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Burning Ship fractal function
def burning_ship(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = complex(abs(z.real), abs(z.imag)) ** 2 + c
        n += 1
    return n

# Generate Burning Ship fractal image
def generate_burning_ship_image(xmin, xmax, ymin, ymax, width, height, max_iter):
    image = np.zeros((height, width))
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)

    for ix in range(width):
        for iy in range(height):
            c = complex(x[ix], y[iy])
            image[iy, ix] = burning_ship(c, max_iter)
    
    return image

# Create animation function
def animate(i, ax, width, height, max_iter):
    # Zooming effect: Faster zoom into the fractal
    scale = 2 ** (i * 0.3)  # Increased zoom speed
    xmin, xmax = -2 / scale, 2 / scale
    ymin, ymax = -2 / scale, 2 / scale

    image = generate_burning_ship_image(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    ax.clear()
    ax.imshow(image, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    ax.set_title(f'Burning Ship Zoom: Iteration {i}')
    ax.axis('off')

# Set up the plot and animation
width, height = 800, 800
max_iter = 256

fig, ax = plt.subplots(figsize=(8, 8))

ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(ax, width, height, max_iter), interval=50)

plt.show()
