import tensorflow as tf

state = tf.Variable(0,name='counter')#定义变量，初始值为0，名字为 counter
# print(state.name)

one=tf.constant(1)#常量1

new_value=tf.add(state,one)#加上一个常量 one
update=tf.assign(state,new_value)#把new_value的值赋给state

init = tf.global_variables_initializer()#初始化所有的变量，如果有定义变量，一定要用这个方式

with tf.Session() as sess:
    sess.run(init) #这一步才是真正的初始化
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))#必须要sess.run() 指针到对应的变量上才能打印出来