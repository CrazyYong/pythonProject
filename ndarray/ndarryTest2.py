import numpy as np


'''
numpy基本操作
'''
#ndarry-数组与标量、数组之间的运算，元素级运算，即只用用于位置相同的元素之间，所得的运算结果组成一个新的数组
#运算结果的位置跟操作位数相同
arr1=np.array([1,2,3,4])
print(arr1+1)

print(arr1-1)

print(2**arr1)

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2,3],[4,5,6]])
print(arr1+arr2)
#ndarray-数组的矩阵积
#矩阵：多维数组即矩阵
#矩阵积：两个二维矩阵（行和列的矩阵）满足第一个矩阵的列数与第二个矩阵的行数相同，那么可以进行矩阵的乘法
#即矩阵积，矩阵积不是元素级的运算。也称为点积、数量积
arr=np.array([[120,60,220],[115,23,201],[132,48,230]])
arr2=np.array([[12.34,0.04],[204.56,2.34],[9.89,0.45]])
print('矩阵积：%s'%(arr.dot(arr2)))
#或者
print('矩阵积第二种方法：%s'%(np.dot(arr,arr2)))

#ndarray-多维数组的索引



'''
ndarray修改形状
对于一个已经存在的ndarray数组对象而言，可以通过修改形状相关的参数/方法从而改变数组的形状
(1)直接修改数组ndarry的shape值，要求修改后乘积不变
(2)直接使用reshape函数创建一个改变尺寸的新数组，原数组的shape保持不变，但是新的数组和原数组
共享一个内存空间，也就是修改任何一个数组中的值都会对另外一个产生影响，另外要求新数组的元素
个数和原数组一致
当指定某一个轴为-1的时候，表示将根据数组元素的数量自动计算该轴的长度值
'''
a=np.arange(0,20,2)
print(a)

b=a.reshape(2,5)#2*5=10,和原数组的元素个数要保持一致
print(b)
print(b.size)
print(b.shape)

b[0][1]=100#修改之后原数组也会发生改变
print(a)
print(b)
print('行轴为-1的时候，根据元素数量自动计算轴的长度%s'%(a.reshape(-1,5)))
print('列轴为-1的时候，根据元素数量自动计算轴的长度%s'%(a.reshape(5,-1)))
print(a.shape)#形状，用于描述当前数组各维度上的数量级别


a.shape=(2,-1) #reshape修的是复制之后的数组形状，但是shape是在原数组修改
print(a)


'''
ndarry中元素数据类型
可以在创建时候给定数据类型或者通过astype设置数据类型
通过astype修改后是一个新数组，和原数组互不影响
'''
a2=np.array([1,2,3,4])
print(a2.dtype)
a3=a2.astype(float)
print(a2.dtype)
print(a3.dtype)

