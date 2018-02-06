import numpy as np


'''
点线
'''
a=np.array([1,2.0,3,4])
print (a.ndim)#ndim查看多少维度
print (a.dtype)#dtype输出的是组成数组的元素的数据类型，int32


'''
面
'''
b=np.array([[1,2,3,4],[1,2,3,4]])
print (b.ndim)


'''
体
'''
c=np.array([
        [
             [1,2.,3,4],
             [1,2.,3,4]
             ],

            [
             [1,2.,3,4],
             [1,2.,3,4]
             ]
            ])

print (c.ndim)#ndim查看多少维度
print (c.dtype)#元素的数据类型，可自动推断与扩充
print (c.shape)#形状，用于描述当前数组各维度上的数量级别
print(c.size)#返回当前数组的元素的总个数，shape返回值的乘积（2*2*4）
print('索引值%d'%(c[0,1,2]))
print('索引值切片%s'%(c[0][1][1:3]))#切片提取数据，冒号取值范围值，是一个左闭右开区间
cc=c[0,:,1:3]
print('冒号在维度上，表示保留该维度的所有数据%s'%(cc))#冒号在维度上，表示保留该维度的所有数据
cc2=c[:,:,1:3]
print('冒号在维度上，表示保留该维度的所有数据%s'%(cc2))#冒号在维度上，表示保留该维度的所有数据
# cc3=c.reshape(4.4)#只更改数组的形状，不对原数组元素，个数产生影响
# cc4=c.reshape(-1)#变成一维


a1=np.zeros((2,4))#创建数组指定形状，数值为0
print(a1)

b1=np.ones((2,4))#创建数组指定形状，数值为1
print(b1)

c2=np.empty((2,4))#创建数组,指定数组，数值为未初始化的垃圾值，无限接近0
print(c2)

d1=np.random.random((3,2,3))
print('random.random创建方式%s'%(d1))


'''
其他创建数组的方式 通过函数计算的方式去创建数组
'''
np.arange(20)
np.arange(10,20)
np.arange(10,20,2)#步长是2，左闭右开区间，参数表示：起始值，终止值，步长


np.linspace(0,10,5)##全闭区间，起始值，终止值，元素个数，等差数列

np.logspace(0,2,5)##全闭区间，起始值，终止值(以指数形式存在)，元素个数，等比数列




'''
numpy的布尔索引
布尔值索引本质上只返回True位置的数据，不考虑逻辑判断的结果
'''


# names=np.array(['A','B','C'])
#
# scores=np.array([[89,99,10,20], [30, 45, 55, 67], [44, 100,99,20]])
# classs=np.array([u'语文',u'数学',u'英语',u'体育',])
#
#
# names=='A'
# print(names)


names=np.array(["Bob","Joe","Will","Bob","Will","Joe","Joe"])
data=np.random.randn(7,4)
names=="Bob"
print(names=="Bob")
# array([ True, False, False,  True, False, False, False], dtype=bool)
print(data[names=="Bob"])


'''
花式索引
'''


'''
通过reshape形式更改数组形状之后生成的新的数组，是原来数组的一个视图
视图与原数组共享
'''