import tensorflow as tf


A = tf.Variable(tf.constant(0.0), dtype=tf.float32)
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(A))
    sess.run(tf.assign(A, 10))
    print(sess.run(A))

#开始给A赋值为0，经过tf.assign函数后，把A的值变为10