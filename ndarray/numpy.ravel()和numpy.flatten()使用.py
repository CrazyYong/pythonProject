import numpy as np
'''
首先声明两者所要实现的功能是一致的（将多维数组降位一维），两者的区别在于返回拷贝（copy）还是返回视图（view），
numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响（reflects）原始矩阵，
而numpy.ravel()返回的是视图（view，也颇有几分C/C++引用reference的意味），会影响（reflects）原始矩阵。
'''
#1两者的功能，默认都是行序优先
x = np.array([[1, 2], [3, 4]])
print(x)

a=x.flatten()
print('flatten():',a)

b=x.ravel()
print('ravel():',b)

print('flatten()列序优先:',x.flatten('F'))
print('ravel()列序优先:',x.ravel('F'))

#2两者的区别
x = np.array([[1, 2], [3, 4]])
x.flatten()[1] = 100 # flatten：返回的是拷贝
print(x)

x.ravel()[1] = 100
print(x)