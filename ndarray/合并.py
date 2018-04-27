import numpy as np

#增加了array的维度，比如一维变二维，二维变三维，三维变思维...,np.newaxis放在那里就在那里增加一维，数组的大小以原数组的大小为基准进行扩展
A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
print(A)

C=np.vstack((A,B)) #上下合并
D=np.hstack((A,B))#左右合并

print(A[:,np.newaxis])#np.newaxis列上加一个维度

C=np.concatenate((A,B,B,A),axis=1)
print(C)