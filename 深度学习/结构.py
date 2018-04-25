import tensorflow as tf
import numpy as np

# create data 预测一个线性的直线（y_data = x_data*0.1 + 0.3）
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

###      create tensorflow structure start     创建结构开始###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))#参数变量，可能是一个矩阵，初始范围-1.0 - 1.0
biases = tf.Variable(tf.zeros([1]))#初始值为0

y = Weights*x_data + biases#预测的y

loss = tf.reduce_mean(tf.square(y-y_data))#预测的y跟实际的y_data的误差

optimizer = tf.train.GradientDescentOptimizer(0.5)#梯度下降 优化器， 0.5表示学习效率，是一个小于0.5的数
train = optimizer.minimize(loss)#用优化器减少误差（每一步都要做）

# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
#初始化整个神经网络的结构
init = tf.global_variables_initializer()  # 替换成这样就好

###       create tensorflow structure end      创建结构结束###

sess = tf.Session()
sess.run(init)          # Very important，激活init

for step in range(401):
    sess.run(train)#开始训练
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))