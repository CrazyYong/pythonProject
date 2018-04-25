import tensorflow as tf

input1 = tf.placeholder(tf.float32) #需要给定一个type
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)#乘法运算

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.0]})) #运行的时候再给定值
