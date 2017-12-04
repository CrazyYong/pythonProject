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


# df1=DataFrame([
#     ['Tom','Gerry','John']
#     ,[76,98,78]
# ])
#
# df2=DataFrame([['Tom',76,],
#                ['Gerry',98],
#                ['John',85]
#                ],columns=[u'姓名',u'成绩'])
#
# print(df2.columns)#列索引
# print(df2.index)#行索引
# print(df2.values)#数据


# data={'arart':['101','102','103','101'],'profits':[589.3,412.2,12.3,25.6],'year':[2001,2005,2010,2015],'month':8}
# df=DataFrame(data)
# df.index=['one','two','three','four']
# # print(df)
# # print(df['year'])#通过列索引
# # print(df.ix['one'])#通过行索引
# df['month']=[5,6,7,8]#修改值
# df['pdn']=np.NaN#新增列
# df.ix['five']=np.NaN#新增行
# print(df)


# df=pd.read_csv("C:/Users/cmx/Desktop/hh.txt",sep=' ')
# print(df)


#数据过滤索引
# data={'arart':['101','102','103','101'],'profits':[589.3,412.2,12.3,25.6],'year':[2001,2005,2010,2015],'month':8}
# df=DataFrame(data)
# columnss=['name','age',u'语文',u'数学']
# df.columns=columnss
# df.ix['new']=np.NaN
# df=df.dropna()#删除NaN行
# # print(df)
# print(df[columnss[2:]])

#缺省值NaN方法处理
df2=DataFrame([['Tom',np.nan,456.67,'M'],['Merry',34,345.66,np.nan]
               ,['Gerry',np.nan,np.nan,np.nan],
               ['John',23,np.nan,'M'],
               ['Joe',18,385.16,'F']],columns=['name','age','salary','gender'])
# print(df2)
# df2=df2.dropna()#默认丢弃只要包含缺失值的行
# print(df2)
# df2=df2.dropna(how='all')#给定只丢弃值全部为缺失值的行
# print(df2)
# df2=df2.dropna(axis=1)#丢弃列
# print(df2)

# df=DataFrame(np.random.randn(7,3))
# print(df)
# df.ix[:3,2]=np.nan
# print(df)
# df.fillna(0)
# print(df)
# df=df.fillna({1:0.5,2:-1,3:1})
# print(df.count(axis=0))


# ser=Series(['a','b','c','a','a','c','b'])
# print(ser)
# print(ser.unique())#去重
# print(ser.value_counts())#统计值的数量，默认按值出现的频率降序排列
# print(ser.value_counts(ascending=False))
# mask=ser.isin(['b','c'])#选出值为‘b’，‘c’的项
# print(mask)



# df=DataFrame({'order_id':['1001','1002','1003','1004','1005'],'member_id':['m01','m02','m01','m02','m02']
#               ,'order_amt':[345,312.2,123,250.2,235]})
# print(df)
# print(u'下单用户Id列表：',df['member_id'].count())



#pandas层次索引
# data = Series([988.44,95859,32554,1235,55555],index=[['2001','2001','2001','2002','2002']
#                             ,[u'苹果',u'香蕉',u'西瓜',u'苹果',u'西瓜']])
# print(data)


# df=DataFrame({'year':[2001,2001,2002,2001,2003],
#               'fruit':['apple','banana','apple','banana','apple']
#               ,'product':[2345,3124,5668,2532,2135],
#               'profits':[233.44,4452.2,1225.2,7845.2,2352.2]})
# print(df)
# df=df.set_index(['year','fruit'])#层次化索引
# print(df)
# print(df.ix[2001])

# print(df.sum(level='year'))


df=DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],
             index=['a','b','c','d'],columns=['one','two'])
print(df)
# print(df.sum(axis=1))
print(df.sum(axis=1,skipna=False))
