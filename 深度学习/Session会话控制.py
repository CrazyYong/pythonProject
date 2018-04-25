import tensorflow as tf

matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2]
                     ,[2]])
product=tf.matmul(matrix1,matrix2)#矩阵乘法,类似numpy中的 np.dot(matrix1,matrix2)

##第一种会话控制
# sess=tf.Session()
# result = sess.run(product)#run完之后，返回product的结果
# print(result)
# sess.close()

##第二种会话控制
with tf.Session() as sess:
    result2 = sess.run(product)  # run完之后，返回product的结果
    print(result2)