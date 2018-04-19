import numpy as np
import pandas as pd

dates =pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print(df)

print(df.dropna())#直接丢掉没有数据的行
print(df.dropna(axis=0,how='any'))#丢掉行，how='any'表示只要有NaN就把这行丢掉
print(df.dropna(axis=1,how='all'))#丢掉列，how='all'表示该列全部为NaN才把这列丢掉
print(df.fillna(value=0))#把有NaN的位置填充为0
print(df.isnull())#查询该数据源是否有NaN,返回True或Fale在每个位置
print(np.any(df.isnull())==True)#可能数据量太大，数据源如果包含为NaN的值，就返回True
