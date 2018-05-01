import tensorflow as tf
'''
tf.reduce_mean(x,axis)函数表示求取矩阵或张量指定维度的平均值。若不指定第二个参数，则在所有
元素中取平均值；若指定第二个参数为0，则在第一维元素上取平均值，即每一列求平均值；若指定第二个参数为
1，则在第二维元素上取平均值，即每一行求平均值
'''
x=[[1.,1.],[2.,2.]]
y=tf.reduce_mean(x)#不指定第二个参数，则所有元素相加除以元素总个数
z=tf.reduce_mean(x,axis= 0)#指定第二个参数为0，则在第一维元素上取平均值，即每一列求平均值
m=tf.reduce_mean(x,axis=1)#若指定第二个参数为1，则在第二维元素上取平均值，即每一行求平均值
with tf.Session() as sess:
    print(sess.run(y))
    print(sess.run(z))
    print(sess.run(m))