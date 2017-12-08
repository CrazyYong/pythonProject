import numpy as np
import pandas as pd
from pandas import Series,DataFrame
'''
关于DataFrame的一些基本操作
注意：通过索引方式返回的列只是相应数据的视图，并不是副本，因此，对返回的Series所做的
任何就地修改全部会反映到源DataFrame上。通过Series的copy方法既可显示地复制列
'''


data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada']
                ,'year':[2000,2001,2002,2001,2002]
                ,'pop':[1.5,1.7,3.6,2.4,2.9]}

df=DataFrame(data)
print('原数组\n',df)
print('获取列名\n',df.columns)
#获取列,也可以df['year']
print('获取某一列\n',df.year)
#批量修改列名
df.index=['one','two','three','four','five']
#也可以用df.ix[0]下标来获取某一行
print('获取某一行\n',df.ix['one'])


df2=DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
print(df2)
#列可以通过赋值的方式进行修改,给debt这列赋值
df2['debt']=16.5
print(df2)

#将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度匹配。如果赋值的是一个Series,就会精确匹配DataFrame的索引
#所有空位都将被填上缺失值
val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
df2['debt']=val
print(df2)

#为不存在的列赋值会创建一个新列。关键字del用于删除列：
df2['eastern']=df2.state=='Ohio'
print(df2)
del df2['eastern']


#字典嵌套字典的方式
#如果讲字典嵌套字典传给DataFrame，它就会被解释为：外层字典的键作为列，内层键作为行索引
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
df3=DataFrame(pop)
print('字典嵌套字典\n',df3)

#如果设置了DataFrame的index和columns的name属性，则这些信息也会被显示出来：
df3.index.name='year'
df3.columns.name='state'
print(df3)
#和Series一样，values属性也会以二位ndarray的形式返回DataFrame中的数据
#如果DataFrame各列数据类型不同，则值数组的数据类型就会选用能兼容所有列的数据类型
print(df3.values)
print(df3.values.dtype)
