import numpy as np

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]

C=np.vstack((A,B)) #上下合并
D=np.hstack((A,B))#左右合并

print(A[:,np.newaxis])#np.newaxis列上加一个维度

C=np.concatenate((A,B,B,A),axis=1)
print(C)