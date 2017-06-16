import numpy as np
import matplotlib.pyplot as plt

x1 = 5 * np.random.rand(40)
x2 = 5 * np.random.rand(40) + 25
x3 = 25 * np.random.rand(20)

x = np.concatenate((x1,x2,x3))

y1 = 5 * np.random.rand(40)
y2 = 5 * np.random.rand(40) + 25
y3 = 25 * np.random.rand(20)

y = np.concatenate((y1, y2, y3))

plt.scatter(x,y, s = [100], marker='^', c='m')

plt.show()
