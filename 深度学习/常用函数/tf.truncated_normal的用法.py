import tensorflow as tf
'''
tf.truncated_normal(shape, mean, stddev) :shape表示生成张量的维度，mean是均值，stddev是标准差。
这个函数产生正太分布，均值和标准差自己设定。
这是一个截断的产生正太分布的函数，就是说产生正太分布的值如果与均值的差值大于两倍的标准差，那就重新生成。
和一般的正太分布的产生随机数据比起来，
这个函数产生的随机数与均值的差距不会超过两倍的标准差，但是一般的别的函数是可能的。
'''

c = tf.truncated_normal(shape=[10, 10], mean=0, stddev=1)

with tf.Session() as sess:
    print(sess.run(c))