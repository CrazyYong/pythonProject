import numpy as np
import pandas as pd
from pandas import Series,DataFrame

obj=Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print(obj)

'''
调用reindex将会根据新索引进行重排，若果当索引值不存在，就引入缺失值
'''
obj2=obj.reindex(['a','b','c','d','e'])
print(obj2)
obj2=obj.reindex(['a','b','c','d','e'],fill_value=0) #给上缺省值为0
print(obj2)

'''
对于时间序列这样的有序数据，重新索引时可能需要做一些插值处理。method选项即可达到此目的
例如，使用ffill可以实现前向填充
'''
'''
reindex的（插值）:
ffill或pad  ：  前向填充（或搬运）值
bfill或backfill : 后向填充（或搬运）值
'''

obj3=Series(['blue','purple','yellow'],index=[0,2,4])
obj3=obj3.reindex(range(6),method='ffill')
print(obj3)


'''
对于DataFrame，reindex可以修改（行）索引、列，或两个都修改，如果仅传入一个序列
，则会重新索引行：
'''
frame=DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d']
                ,columns=['Ohio','Texas','California'])
print(frame)
frame2=frame.reindex(['a','b','c','d'])
print(frame2)

states=['Texas','Utah','California']
print(frame.reindex(columns=states))

#也可以同时对行和列进行重新索引，而插值则只能按行应用
frame3=frame.reindex(index=['a','b','c','d'],method='ffill',
              columns=states)
print(frame3)

#利用ix的标签索引功能，重新索引任务可以变得更简洁：
print(frame.ix[['a','b','c','d'],states])

