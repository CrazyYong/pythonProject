import numpy as np
import pandas as pd
from pandas import Series,DataFrame


df=DataFrame({'key1':['a','a','b','b','a'],
              'key2':['one','two','one','two','one']
              ,'data1':np.random.randn(5)
              ,'data2':np.random.randn(5)})

print('原数组\n',df)

# grouped=df['data1'].groupby(df['key1'])
# print(grouped.mean())

# sizeGroup=df.groupby(['key1','key2']).size()#将列名（也可以是字符串，数字或其他Python对象）用作分组键
# print(sizeGroup)

# for name,group in df.groupby('key1'):
#     print(name)
#     print(group)


print(dict(list(df.groupby('key1')))['b'])
