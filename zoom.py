
# Explanation:
# Mandelbrot Function: This generates the Mandelbrot fractal set based on the
# formula z = z^2 + c.
# It returns the number of iterations until the point escapes a given threshold
# (abs(z) > 2).
# Fractal Image Generation: The generate_mandelbrot_image function creates an
# image of the fractal for a specified region in the complex plane, with resolution
# determined by width and height.
# Animation: The animate function is called for each frame of the animation.
# the animation by updating the image over time.
# Customizing:
# You can adjust the scale value to control the speed and extent of the zoom effect.
# Change max_iter for a more detailed fractal, but keep in mind that higher
# values will increase rendering time.



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Mandelbrot set function
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
# Features
• Using debuggers
• Using 3rd party packages
• Docking user windows
• Special support for Turtle programs
• Specifying program arguments
• Simple mode and expert mode
• Shell
• Plotter
29 
30 
31 
32 
33 
34 
35 
36 
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 

• Assistant
• Birdseye
• Web development with Flask

General topics
• Dealing with errors
• General advice on debugging

Online
There is more information available on Thonny wiki: https://github.com/thonny/thonny/wiki.


        z = z*z + c
        n += 1
    return n

# Function to generate a Mandelbrot image for a given region
def generate_mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter):
    # Create an image (array of pixel values)
    image = np.zeros((height, width))
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)

    for ix in range(width):
        for iy in range(height):
            c = complex(x[ix], y[iy])
            image[iy, ix] = mandelbrot(c, max_iter)
    
    return image

# Create the animation function
def animate(i, ax, width, height, max_iter):
    # Zooming effect: gradually zoom into the center of the fractal
    scale = 2 ** (i * 0.1)  # Change the zoom speed as needed
    xmin, xmax = -2 / scale, 2 / scale
    ymin, ymax = -2 / scale, 2 / scale

    # Generate the fractal image for the current zoom level
    image = generate_mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    # Update the image on the plot
    ax.clear()
    ax.imshow(image, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    ax.set_title(f'Mandelbrot Zoom: Iteration {i}')
    ax.axis('off')

# Set up the plot and animation
width, height = 600, 600
max_iter = 256
fig, ax = plt.subplots(figsize=(8, 8))

ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(ax, width, height, max_iter), interval=10)

# Show the animation
plt.show()
