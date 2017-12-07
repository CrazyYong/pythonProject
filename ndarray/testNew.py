import numpy as np
import pandas as pd
from pandas import Series,DataFrame

'''
https://zhuanlan.zhihu.com/p/21598982
'''

df=DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],'B':['one','one','two','three','two','two','one','three']
             ,'C':[1,2,3,4,5,6,7,8],'D':[10,12,12,13,15,16,17,18]})

print('原数组\n',df)

# grouped=df.groupby('A')
# print(grouped.first())

grouped=df.groupby(['A','B'])
print(grouped.last())
print(grouped['C'])

