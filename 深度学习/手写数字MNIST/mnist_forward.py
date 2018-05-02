import tensorflow as tf

INPUT_NODE=784 #神经网络输入节点784 图片的像素点：28*28=784，是一个包含784个元素的一维数组
OUTPUT_NODE=10 #输出的十个数，每个数表示对应数的索引号出现的概率
LAYER1_NODE=500#隐藏层的节点个数

#regularizer为正则化过程中 参数w在总loss中的比例，即正则化的权重
def get_weight(shape,regularizer):
    w=tf.Variable(tf.truncated_normal(shape,stddev=0.1))
    if regularizer !=None:tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))#正则化参数缓解过拟合
    return w

#偏执
def get_bias(shape):
    b=tf.Variable(tf.zeros(shape))
    return b

def forward(x,regularizer):
    w1=get_weight([INPUT_NODE,LAYER1_NODE],regularizer)
    b1=get_bias([LAYER1_NODE])
    y1=tf.nn.relu(tf.matmul(x,w1)+b1)#使用relu非线性函数作为激活函数

    w2=get_weight([LAYER1_NODE,OUTPUT_NODE],regularizer)
    b2=get_bias([OUTPUT_NODE])
    y=tf.matmul(y1,w2)+b2 #模型
    return y