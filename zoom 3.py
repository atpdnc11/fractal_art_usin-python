import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Sierpinski triangle function (Chaos Game)
def sierpinski_step(points, p, num_points):
    x, y = points[-1]
    random_vertex = np.random.choice([0, 1, 2])
    x_new = (x + p[random_vertex][0]) / 2
    y_new = (y + p[random_vertex][1]) / 2
    points.append([x_new, y_new])
    
    if len(points) > num_points:
        points.pop(0)

# Create animation function
def animate(i, ax, num_points):
    p = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])  # Vertices of an equilateral triangle
    points = [[0.5, 0.5]]  # Start from a point in the middle of the triangle

    # Increase the number of points for each frame (faster animation)
    for _ in range(i * 5):  # Increase the number of points more quickly
        sierpinski_step(points, p, num_points)
    
    ax.clear()
    points_array = np.array(points)
    ax.plot(points_array[:, 0], points_array[:, 1], 'k.', markersize=1)
    ax.set_title(f'Sierpinski Triangle: Step {i}')
    ax.axis('off')
    ax.set_aspect('equal')

# Set up the plot and animation
fig, ax = plt.subplots(figsize=(8, 8))

num_points = 100000  # Number of points to generate

ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(ax, num_points), interval=50)

plt.show()
