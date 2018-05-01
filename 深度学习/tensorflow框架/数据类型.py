import tensorflow as tf

a=tf.constant([1.0,2.0])#定义常数张量
b=tf.constant([3.0,4.0])
result =a+b
print(result)
'''
计算图只描述了计算过程，不计算结果

结果：
Tensor("add:0", shape=(2,), dtype=float32)
"add:0"：名字
shape=(2,)：形状
dtype=float32：数据类型

'''

'''
描述一个神经元
'''
x=tf.constant([[1.0,2.0]])
w=tf.constant([[3.0],[4.0]])

y=tf.matmul(x,w)
print(y)

'''
结果：
Tensor("MatMul:0", shape=(1, 1), dtype=float32)
'''