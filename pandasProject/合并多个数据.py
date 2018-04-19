import numpy as np
import pandas as pd

#concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
res=pd.concat([df1,df2,df3],axis=0)#axis=0列，
print(res)

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#忽略index进行合并
print(res)

#join,['inner','outer']
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)

res=pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)


#join_axes
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
print(res)

#append
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'],index=[2,3,4])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res=df1.append(df2,ignore_index=True)
res=df1.append([df2,df3],ignore_index=True)
#
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)

print(res)