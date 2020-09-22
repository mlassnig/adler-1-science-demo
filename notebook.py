import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu = 0
std = 1

x = np.linspace(start=-4, stop=4, num=100)
y = stats.norm.pdf(x, mu, std) 

plt.plot(x, y)
plt.show()
