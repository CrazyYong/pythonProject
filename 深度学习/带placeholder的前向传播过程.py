#conding:utf-8
#两层简单神经网络（参考笔记过程）
import tensorflow as tf

######################开始定义架构(计算图)#################

#定义输入和参数
#用placeholder实现输入定义(sess.run中喂入一组数据)
x=tf.placeholder(tf.float32) #要喂的数据,也就是特征:[体积，数量],一行二列的张量
w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))#第一层参数1,两行三列的张量
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))#第二层参数2,三行一列的张量

#定义向前传播过程
a=tf.matmul(x,w1) #第一层
y=tf.matmul(a,w2) #第二层

######################结束定义架构(计算图)#################


#用会话计算结果
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()#初始化第一层参数变量，第二层参数变量
    sess.run(init_op)
    print('y is:',sess.run(y,feed_dict={x:[[0.75,0.5]]}))
