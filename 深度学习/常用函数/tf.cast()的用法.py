import tensorflow as tf
import numpy as np
'''
tf.cast(x,dtype)函数表示将参数x转换为指定数据类型
'''

A=tf.convert_to_tensor(np.array([[1,2,3,3],[3,4,5,6]]))
print(A.dtype)

b=tf.cast(A,tf.float32)
print(b.dtype)