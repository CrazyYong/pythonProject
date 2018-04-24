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


#
'''
np.where函数
'''

arr1=np.array([

    [1,2,np.NaN,4],
    [4,5,6,np.NaN],
    [7,8,9,np.inf],
    [np.inf,np.e,np.pi,4]
])

condition=np.isnan(arr1)|np.isinf(arr1)##得到判断条件

print('原始数组')
print(arr1)
print('结果')
print(np.where(condition,0,arr1)) ##将数组中的所有异常数字替换为0，比如将NaN替换为0


#
'''
np.unique函数主要作用是将数组中的元素进行去重操作（也就是只保存不重复的数据）
'''
arr2=np.array([u'图书',u'数码',u'小吃',u'数码',u'女装',u'小吃',u'美食',u'男装',u'数码'])
print('======原始数据=======')
for a in arr2:
    print(a,end='')
print()

arr3=np.unique(arr2)
print('=======去重后的数据======')
for a in arr3:
    print(a,end=' ')
print()