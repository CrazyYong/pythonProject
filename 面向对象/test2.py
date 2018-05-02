import 深度学习.examples.tutorials.mnist.input_data
from 深度学习.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print(type(mnist))