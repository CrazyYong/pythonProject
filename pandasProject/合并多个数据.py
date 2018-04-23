import numpy as np
import pandas as pd

#concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
res=pd.concat([df1,df2,df3],axis=0)#axis=0列，不指定aixs默认按列合并
print(res)

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#忽略index进行合并,会把index重新排序
print(res)

#join,['inner','outer']
'''
join='outer'为预设值，因此未设定任何参数时，函数默认join='outer'。
此方式是依照column来做纵向合并，有相同的column上下合并在一起，其他独自的column各自成列，原本没有值的位置皆以NaN填充。
inner方式表示的是只保留相匹配的的，抛弃不匹配的
'''
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)

res=pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)


#join_axes
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])##依照`df1.index`进行横向合并，那么就只有[1,2,3]这三行，抛弃了df2的第四行
res = pd.concat([df1, df2], axis=1)#移除join_axes，并打印结果
print(res)

#append 只有纵向合并，没有横向合并
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'],index=[2,3,4])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
##将df2合并到df1的下面，以及重置index,并打印结果
res=df1.append(df2,ignore_index=True)

##合并多个df,将df2与df3合并至df1的下面，以及重置index,并打印出结果
res=df1.append([df2,df3],ignore_index=True)

##合并series，将s1合并至df1，以及重置index,并打印出结果
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)

print(res)