from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# arr=np.array([1,3,5,np.NaN,10])
# ser1=Series(arr)
# print(ser1)
# print(ser1.index) #索引index
# print(ser1.values)#值


# ser2=Series([87,88,89])
# print(ser2)

# dict1={'2017333':434.0,'32323':1234.5,'23232':323232.2}
# ser3=Series(dict1)
# print(ser3)

# ser4=Series(data=[88,87,85],index=[u'语文',u'数学',u'英语'],dtype=float)
# print(ser4)
# print(ser4['语文'])
# print(ser4[0:])
# print(ser4['语文':'数学'])


# ser5=Series({'2017333':434.0,'32323':1234.5,'23232':323232.2})
# print(ser5>50000)
# print(ser5/100)
# ser6=Series([-1,-1,-3,4])
# print(np.exp(ser6))
# print(np.fabs(ser6))


# scores=Series({'Tom':89,'John':88,'Merry':96,'Max':65})
# new_index=['Tom','Max','Joe','John','Merry']
# scores=Series(scores,index=new_index)
# scores['Joe']=-1
# print(scores)
# print(pd.isnull(scores))
# print(pd.notnull(scores))
# print(scores[pd.isnull(scores)])
# print(scores[pd.notnull(scores)])


# s1=Series([12,13,34],index=['p1','p2','p3'])
# s2=Series([54,43,32,21],index=['p2','p3','p4','p5'])
# print(s1+s2)



# scores=Series({'Tom':89,'John':88,'Merry':96,'Max':65})
# scores.name=u'语文'
# scores.index.name=u'考试成绩'
# print(scores)


df1=DataFrame([
    ['Tom','Gerry','John']
    ,[76,98,78]
])

df2=DataFrame([['Tom',76,],
               ['Gerry',98],
               ['John',85]
               ],columns=[u'姓名',u'成绩'])

print(df2.columns)#列索引
print(df2.index)#行索引
print(df2.values)#数据