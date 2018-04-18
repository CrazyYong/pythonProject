import numpy as np
import pandas as pd
from pandas import Series,DataFrame

ser1=pd.Series(np.arange(0,4),index=['b','c','d','a'])
print(ser1)
print(ser1.sort_index())#通过列或者行索引进行排序
print(ser1.sort_index(ascending=False))#倒序 由大到小


df1=pd.DataFrame(np.random.randint(1,9,(4,4)),columns=['b','c','a','d'],index=['B','D','A','C'])
print(df1)
print(df1.sort_index())#通过行索引排序，默认从小到大
print(df1.sort_index(axis=1))#通过列索引进行排序
