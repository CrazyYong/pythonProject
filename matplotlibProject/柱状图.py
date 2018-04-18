import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

'''
bar(x,height,width,bottom,*args,align='center',**kwargs)
参数：x数据标量 height:高 width:宽 bottom:底端对应Y轴
align:对齐如果为“居中”，则将X参数解释为条形中心的坐标。如果“边缘”，将条形按其左边缘对齐
要对齐右边缘的条形图，可传递负的宽度和对align='edge'
'''
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

# plt.figure()
plt.bar([1,3,5,7,9,11],[5,2,7,8,2,6],label='Example one',color='y')

plt.bar([2,4,6,8,10,12],[8,6,2,5,6,3],label='Example two',color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title(' ')
plt.show()