import matplotlib.pyplot as plt
import random

x, y = [0], [0]

for _ in range(100000):
    r = random.random()
    if r < 0.01:
        x.append(0)
        y.append(0.16 * y[-1])
    elif r < 0.86:
        x.append(0.85 * x[-1] + 0.04 * y[-1])
        y.append(-0.04 * x[-1] + 0.85 * y[-1] + 1.6)
    elif r < 0.93:
        x.append(0.2 * x[-1] - 0.26 * y[-1])
        y.append(0.23 * x[-1] + 0.22 * y[-1] + 1.6)
    else:
        x.append(-0.15 * x[-1] + 0.28 * y[-1])
        y.append(0.26 * x[-1] + 0.24 * y[-1] + 0.44)

plt.scatter(x, y, s=0.1, color='green')
plt.axis('off')
plt.show()