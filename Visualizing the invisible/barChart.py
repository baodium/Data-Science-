import matplotlib.pyplot as plt

values = [5,8,9,10,4,7]
colors = ['b','r','b','b','r','b']
widths = [0.7,0.8,0.9,0.7,0.7,0.4]
plt.bar(range(0,6), values, color = colors, width=widths)
plt.show()
