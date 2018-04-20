import numpy as np
import pandas as pd

# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
# print(left)
# print(right)
# res=pd.merge(left,right,on='key')#依据key column合并
# print(res)

#consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
##how=['left','right','outer','inner']
res=pd.merge(left,right,on=['key1','key2'],how='inner') #how=inner默认的参数只保留key1,key2有相同的部分，其他舍弃
res=pd.merge(left,right,on=['key1','key2'],how='outer')#不管key1,key2相同不相同，都保留下来，不相同的部分用NaN填充
res=pd.merge(left,right,on=['key1','key2'],how='right')#基于右边的数据的['key1','key2']进行合并，以右边['key1','key2']有的参数为主，如果左边对应的没数据则用NaN进行填充
print(left)
print(right)
print(res)

#indicator
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
res=pd.merge(df1,df2,on='col1',how='outer')
res=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
print(res)

#merged by index 通过index来进行合并
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left)
print(right)

#依据左右资料集的index进行合并，how='outer',并打印出
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
#      A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C2   D2
# K3  NaN  NaN   C3   D3

#依据左右资料集的index进行合并，how='inner',并打印出
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
#     A   B   C   D
# K0  A0  B0  C0  D0
# K2  A2  B2  C2  D2

#suffixes
#定义资料集
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)

#使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
#    age_boy   k  age_girl
# 0        1  K0         4
# 1        1  K0         5