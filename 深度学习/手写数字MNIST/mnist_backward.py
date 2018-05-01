import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
from 深度学习.手写数字MNIST import mnist_forward

BATCH_SIZE=200
LEARNIG_RATE_BASE=0.1
LEARNING_RATE_DECAY=0.99
REGULARIZER=0.0001
STEPS=50000
MOVING_AVERAGE_DECAY=0.99
MODEL_SAVE_PATH='./model/'
MODEL_NAME='mnist_model'

def backward(mnist):
    x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
    y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
    y = mnist_forward.forward(x, REGULARIZER)
    global_step = tf.Variable(0, trainable=False)

    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cem=tf.reduce_mean(ce)
    #包含正则化的损失函数
    loss=cem+tf.add_n(tf.get_collection('losses'))#tf.add_n表示将参数列表内对应元素相加,tf.get_collection('')函数表示从collection集合取出全部变量生成一个列表

    #指数衰减学习率
    learning_rate=tf.train.exponential_decay(LEARNIG_RATE_BASE,global_step,mnist.train.num_examples/BATCH_SIZE
                                             ,LEARNING_RATE_DECAY,staircase=True)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())
    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()#实例化saver用于保存模型

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        for i in range(STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)#每次读取BATCH_SIZE个图片和标签
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})#喂入神经网络并执行
            if i % 1000 == 0:
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)#保存模型，保存当前会话


def main():
    mnist = input_data.read_data_sets("./data/", one_hot=True)
    # backward(mnist)
    # print(mnist.train.num_examples) #返回mnist数据集中训练集train样本数
    # print(mnist.validation.num_examples) #返回mnist数据集中验证集validation样本数
    # print(mnist.test.num_examples)#返回mnist数据集中测试集test样本数
    # print(mnist.train.labels[0])#在mnist数据集中，想要查看训练集中第0张图片的标签
    # print(mnist.train.images[0])#使用train.images函数返回mnist
    xs,ys=mnist.train.next_batch(BATCH_SIZE)#使用mnist.train.next_batch()函数将数据输入到神经网络中
    print('xs shape:',xs.shape)
    print('ys shape:',ys.shape)

if __name__ == '__main__':
    main()
