import tensorflow as tf
'''
线上的权重w,用变量表示，随机给初值
'''
'''
tf..random_normal():正太分布
stddev:标准差
mean:均值
seed:随机种子
'''
w=tf.Variable(tf.random_normal([2,3],stddev=2,mean=0,seed=1))

'''
tf.truncated_normal():去掉过大偏离点的正太分布
'''
w=tf.truncated_normal([2,3])

'''
tf.random_uniform():平均分布
'''
w=tf.random_uniform([2,3])

'''
tf.zeros 全0数组
'''
w=tf.zeros([3,2],dtype=tf.int32)
print(w)

'''
tf.ones 全1数组
'''
w=tf.ones([3,2],dtype=tf.int32)
print(w)

'''
tf.fill 全定值数组
'''
w=tf.fill([3,2],6) #生成：[[6,6],[6,6],[6,6]]

'''
直接给定值
'''
w=tf.constant([3,2,1])