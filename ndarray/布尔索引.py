import numpy as np

'''
numpy的布尔索引
布尔值索引本质上只返回True位置的数据，不考虑逻辑判断的结果
'''


# names=np.array(['Gerry','Tom','John'])
# scores=np.array([[98,87,86,95],
#                  [58,56,54,51],
#                  [78,85,85,77]])
# classs=np.array([u'语文',u'数学',u'英语',u'科学'])
# print('Gerry score is:',scores[names=='Gerry'].reshape(-1))
# print('Gerry 数学 score is:',scores[names=='Gerry'].reshape(-1)[classs==u'数学'])
# print(u'Gerry 和 Tom的成绩-----')
# print(scores[(names=='Gerry')|(names=='Tom')])
# print('非Gerry和Tom学生的成绩')
# print(scores[(names!='Gerry')&(names!='Tom')].reshape(-1))
# print('非Gerry和Tom学生的数学成绩:',scores[(names!='Gerry')&(names!='Tom')].reshape(-1)[classs==u'数学'])


names=np.array(["Bob","Joe","Will","Bob","Will","Joe","Joe"])
data=np.random.randn(7,4)
names=="Bob"
print(names=="Bob")
# array([ True, False, False,  True, False, False, False], dtype=bool)
print(data[names=="Bob"])