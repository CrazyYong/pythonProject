import numpy as np
import pandas as pd
from pandas import Series,DataFrame


##Series 通过一维数组去创建
arr=np.array([1,2,3,4])
ser1=Series(arr)
print(ser1)
print('值%s'%(ser1.values))
print('索引%s'%(ser1.index))##[0,len(arr)-1,1]
ser1.index=['a','b','c','d']
print('修改index后：%s'%(ser1.index))
print(ser1['c'])

ser2=Series([99,100,78,10],index=['a','b','c','d'])
print(ser2)

###通过一维数组在创建时，可以在创建的同时直接自定义索引值，也可以创建之后通过赋值
###的形式去修改

##通过字典创建
##字典本身含有映射关系,所以键不能重复
dict={'a':1,'b':2,'c':3}##通过字典去创建，字典的键对应ser中的索引，字典的值对应ser中的数据
ser3=Series(dict)
print(ser3)

##Series中，元素级别的运算结果，包含有索引值，并且键值关系不会发生改变
ser4=Series([1,2,3,4],index=['a','a','a','a'])
print(ser4)

print(ser4>2)
print(ser4[ser4>2])
print(ser4/100)
print(ser4['a'])


##numpy种的通用函数在Series中也是支持的
ser5=Series([-1,-2,-3,-4])
print(np.abs(ser5))
print(ser4[:1].index)


##自动对齐：键值对关系不发生改变。如果键无法对应，则返回值Nan
ss=Series({'a':100,'b':99,'c':120,'d':323})
print(ss)
new=['a','b','eeee','c','d']
ss_new=Series(ss,index=new)
print(ss_new)


print(pd.isnull(ss_new))##Nan值返回True
print('返回值%s'%(ss_new[pd.isnull(ss_new)]))


##按照索引的形式找到与之相匹配的数据做对应操作
s1=Series([1,2,3],index=['a','b','c'])
s2=Series([10,20,30,40],index=['a','b','c','d'])
print('相加结果%s'%(s1+s2))

s1.name=u'价格' ##s1.name 数据名称标签
s1.index.name=u'产品'##s1.index.name 索引名称标签
print(s1)


