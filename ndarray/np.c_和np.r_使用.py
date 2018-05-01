import numpy as np

'''
np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。
np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
'''

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.c_[a,b]

# print(np.r_[a,b])
# print(c)
# print(np.c_[c,a])

'''
np.r_
二维数组比较明显，就是按列来连接
'''
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
print('二维np.r_结果:',np.r_[a,b])

'''
np.c_
二维数组比较明显，就是按行来连接
'''
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
print('二维np.c_结果:',np.c_[a,b])
'''
结果：
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
'''