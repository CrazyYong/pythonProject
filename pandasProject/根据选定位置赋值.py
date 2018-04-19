import numpy as np
import pandas as pd

dates =pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[2,2]=1111#根据下标选择第二行第二列选择，然后赋值
df.loc['20130101','B']=222#根据索引选择，然后赋值
df[df.A>4]=0#boolean选择，统一更改
df.A[df.A>4]=0#对 A这一列，大于4的统一赋值为0
df.B[df.A>4]=0#对 B这一列中，A大于4的统一赋值为0
df['F']=np.nan# 没有‘F’ 这一列，会自动补充
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))#可以加入一个Series，但是index要和源数据的index相同，不然会赋值NaN

print(df)