import numpy as np

'''
二位数组的情况下，axis=0表示对同列的数据进行聚合；axis=1表示对同行的数据进行聚合
'''
arr=np.array([[1,2,3,4],[7,8,9,10]])
print('arr=',arr)
print('min=',arr.min(axis=0))#非NA的最小值
print('max=',arr.max())#非NA的最大值
print('mean=',arr.mean())#非NA值的平均数
print('std=',arr.std())#无偏（分母为n-1）标准差和方差
print(u'根据方差公式计算的方差值为:',np.sqrt(np.power(arr-arr.mean(),2).sum()/arr.size))