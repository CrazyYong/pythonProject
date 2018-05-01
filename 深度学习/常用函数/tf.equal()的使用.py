import tensorflow as tf
import numpy as np
'''
tf.equal()函数表示对比两个矩阵或者向量的元素。若对应元素相等，则返回True;若对应元素不相等，则返回False
'''

A=[[1,3,4,5,6],[4,5,6,7,8]]
B=[[1,2,3,5,6],[8,7,4,8,4]]

with tf.Session() as sess:
    print(sess.run(tf.equal(A,B)))