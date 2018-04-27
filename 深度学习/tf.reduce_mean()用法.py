import tensorflow as tf

'''
函数作用： 
沿着tensor的某一维度，计算元素的平均值。由于输出tensor的维度比原tensor的低，这类操作也叫降维。

参数： 
reduce_mean(input_tensor,axis=None,keep_dims=False,name=None, reduction_indices=None) 
input_tensor：需要降维的tensor。 
axis：axis=none, 求全部元素的平均值；axis=0, 按列降维，求每列平均值；axis=1，按行降维，求每行平均值。 
keep_dims：若值为True，可多行输出平均值。 
name：自定义操作的名称。 
reduction_indices：axis的旧名，已停用。

返回： 
降维后的tensor
'''
x = tf.constant([[1., 2., 3.], [4., 5., 6.]])

with tf.Session() as sess:
    x = sess.run(x)

    mean1 = sess.run(tf.reduce_mean(x))
    mean2 = sess.run(tf.reduce_mean(x, 0))
    mean3 = sess.run(tf.reduce_mean(x, 1))

    print(x)
    print()
    print(mean1)
    print()
    print(mean2)
    print()
    print(mean3)