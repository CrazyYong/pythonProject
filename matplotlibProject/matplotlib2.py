import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(8,6))
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(),'k--')
ax1.hist(np.random.randn(300),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
plt.show()