import tensorflow as tf
import numpy as np
'''
tf.cast(x,dtype)函数表示将参数x转换为指定数据类型
'''

A=tf.convert_to_tensor(np.array([[1,2,3,3],[3,4,5,6]]))
print(A.dtype)

b=tf.cast(A,tf.float32)
print(b.dtype)


x=[[1.,1.],[2.,2.]]
z=tf.reduce_mean(x,axis= 0)#指定第二个参数为0，则在第一维元素上取平均值，即每一列求平均值
b=tf.cast(z,tf.float32)

A=[[1,3,4,5,6],[4,5,6,7,8]] #预测结果
B=[[1,2,3,5,6],[8,7,4,8,4]] #实际喂入的结果

correct_prediction = tf.equal(A, B)
castResult=tf.cast(correct_prediction, tf.float32)
accuracy = tf.reduce_mean(castResult)

with tf.Session() as sess:
    # print(sess.run(z))
    # print(sess.run(b))
    print(sess.run(correct_prediction))
    print(sess.run(castResult))
    print(sess.run(accuracy))