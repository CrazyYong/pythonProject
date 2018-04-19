import numpy as np

A=np.arange(12).reshape((3,4))
print(A)

'''
等量的分割
split(arr,分成的块数，轴),块数要是平均分配的，比如有一个三行四列的数组，按行分，可以分成2块，4块，但是不可以分成三块
'''
print(np.split(A,1,axis=1))

'''
不等量的分割
'''
# print(np.array_split(A,3,axis=1))

'''
纵向分割：vsplit(arr,块数)
横向分割:hsplit(arr,块数)
'''
print(np.vsplit(A,3))
print(np.hsplit(A,2))