import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
T=np.random.rand(8)*125
plt.scatter(x,y,label='散点分布',c=T,s=25,marker='o',alpha=0.5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('散点图')
plt.legend()
plt.show()
