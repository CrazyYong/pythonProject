import numpy as np
import pandas as pd
from pandas import Series,DataFrame


##通过二维数组去创建
df=DataFrame([
                ['a','b','c','d'],
                [1,2,3,4]
                    ])

print(df)

darr=np.array([
                [1,2,3,4],
                [2,3,4,5],
                [3,4,5,6]
                    ])
df2=DataFrame(darr,index=['one','two','three'],columns=['a','b','c','d'])##行索引
print(df2)
print(df2.values)

##通过字典创穿件DataFrame,字典的键作为DataFrame的索引，值作为DataFrame的列数据
dict1={'apart':['101','102','101'],
       'profits':[1000,2000,3000],
       'year':[2001,2002,2002],
       'month':8}

df3=DataFrame(dict1)
print(df3)
print(df3.index)
print(df3.columns)

df3.index=['one','two','three']
print(df3)


# df4=pd.read_csv("C:/Users/admin/Desktop/data2.csv")
# print(df4)

df5=pd.read_csv("data02.txt")
print(df5)