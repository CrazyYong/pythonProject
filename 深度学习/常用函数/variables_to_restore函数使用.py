import tensorflow as tf

#1、滑动平均值模型文件的保存
if __name__ == "__main__":
    v = tf.Variable(0., name="v")
    # 设置滑动平均模型的系数
    ema = tf.train.ExponentialMovingAverage(0.99)
    # 设置变量v使用滑动平均模型，tf.all_variables()设置所有变量
    op = ema.apply([v])
    # 获取变量v的名字
    print(v.name)
    # v:0
    # 创建一个保存模型的对象
    save = tf.train.Saver()
    sess = tf.Session()
    # 初始化所有变量
    init = tf.initialize_all_variables()
    sess.run(init)
    # 给变量v重新赋值
    sess.run(tf.assign(v, 10))
    # 应用平均滑动设置
    sess.run(op)
    # 保存模型文件
    save.save(sess, "./model/model.ckpt")
    # 输出变量v之前的值和使用滑动平均模型之后的值
    print(sess.run([v, ema.average(v)]))
    # [10.0, 0.099999905]




    #3、variables_to_restore函数的使用
    v = tf.Variable(1., name="v")
    # 滑动模型的参数的大小并不会影响v的值
    ema = tf.train.ExponentialMovingAverage(0.99)
    print(ema.variables_to_restore())

    ema_restore = ema.variables_to_restore()

    sess = tf.Session()
    saver = tf.train.Saver(ema_restore)
    # saver.restore(sess, "./model/model.ckpt")
    # print(sess.run(v))

    ckpt = tf.train.get_checkpoint_state('./model/')  # 把滑动平均值赋给各个参数
    saver.restore(sess, ckpt.model_checkpoint_path)  # 恢复模型到当前会话

    # 0.0999999


