import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')


x = [1, 2, 3, 4, 5]
y = [100, 200, 300, 400, 500]

plt.bar(x, y)

plt.show()
