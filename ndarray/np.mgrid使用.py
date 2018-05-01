import numpy as np

'''
np.mird[起:止:步长,起:止:步长]
产生的结果为双矩阵。

步长为复数表示点数，左闭右闭
步长为实数表示间隔，左闭右开

mgrid[[1:3:3j, 4:5:2j]] 
3j：表示三个点
'''
X1,Y1=np.mgrid[1:3:3j,4:5:2j]
print(X1)
print(Y1)

'''
np.orgid[起:止:步长,起:止:步长]
产生结果为一维数组（列向量和行向量）
'''
X1,Y1=np.ogrid[1:4:4j,4:5:3j]
print(X1)
print(Y1)