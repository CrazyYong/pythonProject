import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#创建一组数据量为30，步长为1，形状为5行6列的数组
#一般请款下arange搭配reshape使用，用于把创建好的一维数组重塑为特定数组
arr=np.arange(30).reshape(5,6) #创建一个四行五列的数组
print(arr)