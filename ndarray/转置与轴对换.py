import numpy as np

'''
数组转置
'''
arr=np.arange(40).reshape(5,-1) #shape为(5,8)
print(arr.shape)

arr1=arr.transpose()#转置shape为(8,5),元素坐标的转置
print(arr1.shape)

#T,适用于一、二维数组
arr2=arr.T#转置shape为(8,5)
print(arr2.shape)

'''
transpose
数组轴对换
我是这样的理解的，比如说三维的数组，那就对维度进行编号，也就是0,1,2。
这样说可能比较抽象。这里的0,1,2可以理解为对shape返回元组的索引。
'''
arr1=np.random.randint(0,10,(4,3,2))
print(arr1)

arr1.transpose(1,2,0) #轴变换


'''
swapaxes轴对换
swapaxes接受一对轴编号，其实这里我们叫一对维度编号更好吧，比如：
'''
arr=np.arange(16).reshape((2,2,4))
arr.swapaxes(2,1)  #就是将第三个维度和第二个维度交换