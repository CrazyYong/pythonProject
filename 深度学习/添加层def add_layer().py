import tensorflow as tf
import numpy as np

#加入一个神经层
def add_layer(inputs,in_size,out_size,activation_function=None):
    #因为在生成初始参数时，随机变量(normal distribution)会比全部为0要好很多，
    # 所以我们这里的Weights为一个in_size行, out_size列的随机变量矩阵
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]+0.1))#在机器学习中，biases的推荐值不为0，所以我们这里是在0向量的基础上又加了0.1
    Wx_plus_b=tf.matmul(inputs,Weights)+biases#Wx_plus_b, 即神经网络未激活的值  tf.matmul()是矩阵的乘法。
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]
'''
正态分布
numpy.random.normal(loc=0.0, scale=1.0, size=None)
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape，默认为None，只输出一个值
'''
noise = np.random.normal(0,0.05,x_data)#加入一些噪点让数据更真实 np.random.normal()正态分布
y_data=np.square(x_data)-0.5+noise #np.square() 平方


