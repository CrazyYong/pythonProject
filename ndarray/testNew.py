import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# df = pd.DataFrame({'key1':list('aabba'),
#                   'key2': ['one','two','one','two','one'],
#                   'data1': np.random.randn(5),
#                   'data2': np.random.randn(5)})
#
# print('原数组\n',df)
#
# grouped = df['data1'].groupby(df['key1']) #按key1进行分组并计算data1列的平均值
# print('按key1进行分组,并计算data1列的平均值\n',grouped.mean())
#
#
# means = df['data1'].groupby([df['key1'], df['key2']]).mean()
# print('按key1和key2进行分组,并计算data1的平均值\n',means)




# df=DataFrame({'year':[2001,2001,2002,2002,2003]
#                 ,'fruit':['apple','banana','apple','banana','apple']
#                 ,'production':[2345,3124,5668,2352,2135]
#                 ,'profits':[233.44,4452.2,1225.2,7845.2,2352.2]})
# print(df)
#
# df=df.set_index(['year','fruit'])
# print('层次化索引\n',df)
#
# print('根据索引取值\n',df.ix[2002,'apple'])

# data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],
#                                          [1,2,3,1,2,3,1,2,2,3]])
#
#
# print('原数组\n',data)
# print('降维之后\n',data.unstack())
# print('降维是可逆的\n',data.unstack().stack())
frame = DataFrame(np.arange(12).reshape((4,3)),
                  index=[['a','a','b','b'],[1,2,1,2]],
                  columns=[['Ohio','Ohio','Colorado'],
                           ['Green','Red','Green']])
frame.index.names=['key1','key2']
frame.columns.names = ['state','color']
print(frame)