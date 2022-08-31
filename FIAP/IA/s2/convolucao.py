import numpy as np
from matplotlib import pyplot as plt

a = [1,1,1,1]
b=[1,1,1,1]

c = np.convolve(a,b)

plt.plot(c)

plt.show()