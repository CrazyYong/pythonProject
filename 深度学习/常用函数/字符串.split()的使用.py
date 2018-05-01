'''
字符串.split()函数表示按照指定'拆分符'对字符串拆分，返回拆分列表
'''

x='./model/mnist_model-1001'.split('/')[-1].split('-')[-1]
print(x)