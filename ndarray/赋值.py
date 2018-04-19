import numpy as np
a=np.arange(4)
print(a)

'''
b,c,d就是a，a的改变也会影响b,c,d。
b,c,d改变也会影响a
'''
b=a
c=a
d=b

a[0]=11
print(a)

print(b is a)

'''
deep copy
只把值拷贝过来，而不是关联起来
a的改变不会影响到b，b的改变不会影响a
'''
b=a.copy()