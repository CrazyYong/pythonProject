import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
'''
Subplot:子图，figure对象下创建一个或多个subplot对象（即axes）用于绘制图像
'''
# x1=[1,2,3]
# y1=[5,7,4]
# x2=[1,2,3]
# y2=[10,14,12]
# plt.subplot(221)
# plt.plot(x1,y1,'r-')
# plt.subplot(223)
# plt.plot(x2,y2,'b--')
# plt.show()

####################
# mpl.rcParams['font.sans-serif']=['SimeHei']
# mpl.rcParams['axes.unicode_minus']=False
#
# #获取figure对象
# fig=plt.figure(figsize=(8,6))
# #在figure上创建对象
# ax1=fig.add_subplot(221)
# ax2=fig.add_subplot(222)
# ax3=fig.add_subplot(223)
#
# #在ax1上绘图
# ax1.plot(np.random.randn(50).cumsum(),'g-')
# #在ax2上绘图
# ax2.plot(np.random.randn(50).cumsum(),'b--')
# #在ax3上绘图
# ax3.plot(np.random.randn(50).cumsum(),'k--')
#
# plt.show()

#####################
fig,axes=plt.subplots(2,2)

for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(100),10,color='g',alpha=0.75)
fig.subplots_adjust(wspace = 0,hspace=0)#调整子图之间的距离
plt.show()