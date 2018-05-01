import tensorflow as tf

'''
tf.add_n表示将参数列表内对应元素相加
'''
x=tf.constant([[1,2],[1,2]])
y=tf.constant([[1,1],[1,2]])
z=tf.add_n(x,y)
with tf.Session() as sess:
    print(sess.run(z))

'''
tf.add_n([p1, p2, p3....])函数是实现一个列表的元素的相加。就是输入的对象是一个列表，列表里的元素可以是向量，矩阵
'''
input1 = tf.constant([1.0, 2.0, 3.0])
input2 = tf.Variable(tf.random_uniform([3]))
output = tf.add_n([input1, input2])

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(input1 + input2))
    print(sess.run(output))