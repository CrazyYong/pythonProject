import numpy as np

arr1=np.array([1,2,8,1])
arr2=np.array([4,5,6,0])

##
print(np.mod(arr2,arr1))#元素级的求模计算（除法取余）
##
print(np.dot(arr1,arr2))#求两个数组的点积，等价于矩阵乘法
#
'''
greater、greater_equal、less、less_qual、equal、not_equal：执行元素级别的比较运算，最终返回一个布尔型数组
logical_an、logical_or、logical_xor：执行元素级别的布尔逻辑运算，相当于中缀运算符&、|、^
poser:求解对数组中的每个元素进行给定次数的指数值，类似于：arr**3
'''

