import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False


#展现出100000个随机数满足 平均值是100 标准差是15 呈现一个正态分布的曲线
mu,sigma=100,15
x=mu+sigma*np.random.randn(10000)

plt.hist(x,100,normed=1,facecolor='g',alpha=0.75)

plt.title('直方图')
plt.text(60,0.025,r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()