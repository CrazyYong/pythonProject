import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math


#解决中文输出问题
mpl.rcParams['font.sans-serif']=[u'Simhei']
mpl.rcParams['axes.unicode_minus']=False

x=np.arange(0.05,3,0.05)

#常函数
y1=[5 for i in x]
plt.plot(x,y1,linewidth=2,label='常函数:y=5')

#一次函数
y2=[2*i+1 for i in x]
plt.plot(x,y2,linewidth=2,label='一次函数:y=2x+1')

#二次函数
y3=[1.5*i*i-3*i+1 for i in x]
plt.plot(x,y3,linewidth=2,label='二次函数:y=1.5$x^2$-3x+1')


#幂函数
y4=[math.pow(i,2) for i in x]
plt.plot(x,y4,linewidth=2,label='幂函数:y=$x^2$')

plt.legend(loc='lower right')
plt.grid(True)

plt.show()