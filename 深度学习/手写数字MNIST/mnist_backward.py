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

#反向传播完成对网络参数的训练
def backward(mnist):
    x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
    y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
    y = mnist_forward.forward(x, REGULARIZER)#定义向前传播函数

    global_step = tf.Variable(0, trainable=False)

    #交叉熵自定义损失函数
    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cem=tf.reduce_mean(ce)
    #loss=交叉熵损失函数+正则化损失函数（防止过拟合）
    # tf.add_n表示将参数列表内对应元素相加,tf.get_collection('')函数表示从collection集合取出全部变量生成一个列表
    loss=cem+tf.add_n(tf.get_collection('losses'))

    #指数衰减学习率
    #使用指数衰减学习率可以使模型在训练的前期快速收敛接近较优解，又可以保证模型在训练后期不会有太大波动
    learning_rate=tf.train.exponential_decay(LEARNIG_RATE_BASE,global_step,mnist.train.num_examples/BATCH_SIZE
                                             ,LEARNING_RATE_DECAY,staircase=True)

    #反向传播训练方法 梯度下降
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    #滑动平均值
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    ema_op = ema.apply(tf.trainable_variables())

    #该函数实现将滑动平均和训练过程同步运行
    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    # 实例化saver用于保存模型
    saver = tf.train.Saver()

    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        #实现断点续训
        ckpt=tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess,ckpt.model_checkpoint_path)#把ckpt恢复到当前会话

        for i in range(STEPS):
            # 每次读取BATCH_SIZE个图片和标签
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            # 喂入神经网络并执行
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})
            if i % 1000 == 0:
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                # 保存模型，保存当前会话
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)


def main():
    mnist = input_data.read_data_sets("./data/", one_hot=True)
    backward(mnist)
    # 返回mnist数据集中训练集train样本数
    # print(mnist.train.num_examples)
    # 返回mnist数据集中验证集validation样本数
    # print(mnist.validation.num_examples)
    # 返回mnist数据集中测试集test样本数
    # print(mnist.test.num_examples)
    # 在mnist数据集中，想要查看训练集中第0张图片的标签
    # print(mnist.train.labels[0])
    # 使用train.images函数返回mnist
    # print(mnist.train.images[0])
    # 使用mnist.train.next_batch()函数将数据输入到神经网络中
    # xs,ys=mnist.train.next_batch(BATCH_SIZE)
    # print('xs shape:',xs.shape)
    # print('ys shape:',ys.shape)

if __name__ == '__main__':
    main()
