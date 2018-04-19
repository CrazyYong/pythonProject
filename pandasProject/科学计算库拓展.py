import numpy as np
import pandas as pd
from pandas import Series,DataFrame

'''
sort_index
'''
ser1=pd.Series(np.arange(0,4),index=['b','c','d','a'])
print(ser1)
print(ser1.sort_index())#通过列或者行索引进行排序
print(ser1.sort_index(ascending=False))#倒序 由大到小


df1=pd.DataFrame(np.random.randint(1,9,(4,4)),columns=['b','c','a','d'],index=['B','D','A','C'])
print(df1)
print(df1.sort_index())#通过行索引排序，默认从小到大
print(df1.sort_index(axis=1))#通过列索引进行排序

'''
sort_value
'''
print(ser1.sort_values)
print(df1.sort_values(by=['d','b']))#先按列'd'升序排列，后按'b'降序

'''
rank排序
排名（ranking）跟排序关系密切，且它会增设一个排名值（从1开始，一直到数组中有效数据的数量）
默认情况下，rank是通过“为各组分配一个平均排名”的方式破坏平级关系的
'''
ser=pd.Series([3,4,1,3,3],index=list('abcde'))
print(ser)
print(ser.rank())
print(ser.rank(method='min'))
print(ser.rank(method='max'))
print(ser.rank(method='first'))
df=pd.DataFrame(np.random.randint(0,5,[4,4]))
print(df)
print(df.rank())
print(df.rank(axis=1))

'''
数据统计，用于计算一个Series中各值出现的频率
'''
obj=pd.Series(list('cadaabbcc'))
print(obj.value_counts())

'''
pandas分组
'''
##groupy对DataFrame进行数据分组，传入列名列表或者Series序列对象，返回生成一个GroupBy对象。它实际上还没进行任何计算
data=pd.DataFrame({'key1':list('aabba'),
                   'key2':['one','two','one','two','one']
                  ,'data1':np.random.randn(5)
                  ,'data2':np.random.randn(5)})
grouped=data['data1'].groupby(data['key1'])
print(data)
print(grouped.mean())
means = data['data1'].groupby([data['key1'],data['key2']]).mean()
print(means)
print(means.unstack())