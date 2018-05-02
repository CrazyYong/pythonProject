#coding:utf-8
import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from 深度学习.手写数字MNIST import mnist_forward
from 深度学习.手写数字MNIST import mnist_backward
TEST_INTERVAL_SECS = 5 #定义程序循环的间隔时间是5秒

def test(mnist=input_data.read_data_sets("./data/", one_hot=True)):
    #用tf.Graph().as_default复现计算图
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])#喂入的x值
        y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])#喂入的y_值
        #前向传播得到预测结果y
        y = mnist_forward.forward(x, None)

        #在保存模型时，若模型中采用滑动平均，则参数的滑动平均值会保存在相应文件中。通过实例化saver对象，实现参数滑动平均值的加载
        ema = tf.train.ExponentialMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)#滑动平均基数
        #通过使用variables_to_restore函数，
        # 可以使在加载模型的时候将影子变量直接映射到变量的本身，
        # 所以我们在获取变量的滑动平均值的时候只需要获取到变量的本身值而不需要去获取影子变量
        ema_restore = ema.variables_to_restore()
        #实例化可滑动平均的saver
        saver = tf.train.Saver(ema_restore)

		#神经网络模型准确率评估方法
        #计算正确率
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))#得到一个小于1的概率用于评测模型准确性

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_backward.MODEL_SAVE_PATH)#加载训练好的模型
                if ckpt and ckpt.model_checkpoint_path:#如果已有ckpt模型则回复
                    # 恢复会话
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    # 恢复轮数
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    #计算准确率
                    accuracy_score = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
                    print("After %s training step(s), test accuracy = %g" % (global_step, accuracy_score))
                else:
                    print('No checkpoint file found')
                    return
            time.sleep(TEST_INTERVAL_SECS)

def main():
    # mnist = input_data.read_data_sets("./data/", one_hot=True)
    test()

if __name__ == '__main__':
    main()
