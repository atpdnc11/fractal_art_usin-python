import matplotlib.pyplot as plt
import random

x, y = [0], [0]

for _ in range(100000):
    r = random.random()
    if r < 0.33:
        x.append(0.5 * x[-1])
        y.append(0.5 * y[-1])
    elif r < 0.66:
        x.append(0.5 * x[-1] + 0.5)
        y.append(0.5 * y[-1])
    else:
        x.append(0.5 * x[-1] + 0.25)
        y.append(0.5 * y[-1] + 0.5)

plt.scatter(x, y, s=0.1, color='purple')
plt.axis('off')
plt.show()