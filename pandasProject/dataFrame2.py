import numpy as np
import pandas as pd
from pandas import Series,DataFrame

'''
索引对象
'''

'''
pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。构建Series或DataFrame时
，所用到的任何数组或其他序列的标签都会被转化成一个Index
'''
'''
Index对象是不可修改的，因此用户不能对其进行修改
不可修改非常重要，因为这样才能使Index对象在多个数据
'''
obj=Series(range(3),index=['a','b','c'])
index=obj.index
print(obj)
print(index)
print(index[1:])

'''
不可修改非常重要，因为这样才能使Index对象在多个数据
'''
index=pd.Index(np.arange(3))
obj2=Series([1.5,-2.5,0],index=index)
print(obj2.index is index)

'''
每个索引都有一些方法和属性，它们可以设置逻辑并回答有关该索引所包含的数据的常见问题
参考OneNote
'''
