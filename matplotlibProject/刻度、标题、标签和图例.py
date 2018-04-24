import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

x1=[1,2,3]
y1=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x1,y1,'ro--',label='First Line')#设置线条标签
plt.plot(x2,y2,'b-',label='Second Line')
#设置标题、标签
plt.xlabel('月份')#X轴标签
plt.ylabel('年份')#Y轴标签
plt.title('进出口数据')#标题
#设置X轴范围
plt.xlim(1,3)
#设置Y轴范围
plt.ylim(0,15)
#设置X轴刻度
plt.xticks(np.linspace(0,6,5))
#设置Y轴刻度
plt.yticks(np.arange(1,15,3),['2011年','2012年','2013年','2014年','2015年'])
#获取坐标轴信息 gca='get current axis'
ax=plt.gca()
#设置边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#legend 生成默认图例
plt.legend(loc='best')
'''
另一种构造图例的方式
pl1,=plt.plot(x1,y1,'ro--')#设置线条标签
pl2,=plt.plot(x2,y2,'b-')
plt.legend(handles=[pl1,pl2,],labels=['aaa','bbb'],loc='best')
'''
plt.show()