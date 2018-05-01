import tensorflow as tf
'''
tf.argmax(x,axis)函数表示返回指定维度axis下，参数x中最大值索引
'''
x=[[1.,4.],[5.,6.]]
y=tf.argmax(x,axis=0)#axis=0表示列维度下，x中最大值的索引
z=tf.argmax(x,axis=1)#axis=1表示行维度下，y中最大值的索引

with tf.Session() as sess:
    print(sess.run(y))
    print(sess.run(z))
