import numpy as np

# arr1=np.array([
#     [
#         [1,2,3],[4,5,6]
#     ]
#     ,
# [
#         [7,8,9],[10,11,12]
#     ]
#     ,
# [
#         [13,14,15],[16,17,18]
#     ]
# ]
# )



# print(arr1[:,0:,0])


# arr2=np.arange(32).reshape(8,4)
# print(arr2)
# print(arr2[[0,3]]) #获取第0行第3行数据
# print(arr2[[0,3,5],[0,3,2]])#h获取第（0,0），（3,3），（5,2）这三个索引位置的数据[0,15,22]
# print(arr2[np.ix_([0,3,5],[0,3,2])])

# arr3=np.arange(40).reshape(5,-1)
# print(arr3.shape)
#
# arr4=arr3.transpose()
# arr5=arr3.T
# print(arr5.shape)

# arr6=np.array([-5.3,-6.2,-4.3])
# print(np.fabs(arr6))

# arr7=np.array([
#     [1,2,3,4],
#     [7,8,9,10]])
# print(arr7)
# print(arr7.min())
# print(arr7.max())
# print(arr7.mean())
# print(arr7.min(axis=0))#二维数组的情况下，axis=0表示对同列的数据进行聚合；axis=1表示对同行的数据进行聚合
# print(arr7.sum(axis=1))




# xarr=np.array([-1.1,-1.2,-1.3,-1.4,-1.5])
# yarr=np.array([-2.1,-2.2,-2.3,-2.4,-2.5])
# condition=xarr<yarr
# print(condition)
# result1=[x if c else y for (x,y,c) in zip(xarr,yarr,condition)]
# print(result1)
# result2=np.where(condition,xarr,yarr)
# print(result2)

# arr8=np.array([[1,2,np.NaN,4],[4,5,6,np.NaN],
#              [7,8,9,np.inf],
#              [np.inf,np.e,np.pi,4]])
# condition=np.isnan(arr8)|np.isinf(arr8)
# print(np.where(condition,0,arr8))


arr=np.array([u'图书馆',u'数码',u'小吃',u'数码',u'女装',u'小吃',u'美食',u'男装'
              u'数码'])
# print(arr)
arr2=np.unique(arr)
print(arr2)
