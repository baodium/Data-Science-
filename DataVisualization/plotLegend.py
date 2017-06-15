import matplotlib.pyplot as plt

line1 = plt.plot(range(1,11), values)
line2 = plt.plot(range(1,11), values2)

plt.legend(['First', 'Second'], loc=4)

plt.show()
