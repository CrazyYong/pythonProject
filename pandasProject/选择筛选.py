import numpy as np
import pandas as pd

dates =pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
# print(df['A'],df.A)
# print(df[0:3],df['20130102':'20130104'])

#select by label:loc 根据索引选择
print(df.loc['20130102']) #选择 ‘20130102’ 这一行
print(df.loc[:,['A','B']])
print(df.loc['20130102',['A','B']])

#select by position:iloc 根据下标选择
print(df.iloc[3,1])#选择第三行，第一列的数据
print(df.iloc[[1,3,5],1:3])

#mixed selection:ix ，混合筛选，可以根据下标和索引同时筛选
print(df.ix[:3,['A','C']])

#Boolean indexing 进行一个boolean筛选
print(df[df.A>8])