import numpy as np
'''
随机数生成器,seed为随机种子，只要随机种子seed相同，产生的随机数序列就相同
'''
seed=2
rdm = np.random.RandomState(seed)
X=rdm.randn(3,2)
print(X)

Y_=[int(x0*x0+x1*x1<2) for x0,x1 in X]
print(Y_)
# Y_c=[['red' if y else 'blue'] for y in Y_]
# print(Y_c)
Y=np.vstack(Y_).reshape(-1,1)
print(Y)
