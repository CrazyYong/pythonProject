import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x = np.arange(20)
y = x**3

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

plt.show()