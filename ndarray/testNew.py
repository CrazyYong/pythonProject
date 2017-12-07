import numpy as np
import pandas as pd
from pandas import Series,DataFrame

'''
https://zhuanlan.zhihu.com/p/21598982
'''

df=DataFrame({'key1':['a','a','b','b','a'],
              'key2':['one','two','one','two','one']
              ,'data1':np.random.randn(5)
              ,'data2':np.random.randn(5)})
