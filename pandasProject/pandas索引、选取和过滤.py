import numpy as np
import pandas as pd
from pandas import Series,DataFrame

obj=Series(np.arange(4.)
           ,index=['a','b','c','d'])
# print(obj['b'])
# print(obj[2:4])
print(obj[[1,3]]) #第一行，第三行
#利用标签的切片与普通的Python切片运算不同，其末端是包含的
obj['b':'c']=5
print(obj)


data=DataFrame(np.arange(16).reshape((4,4))
               ,index=['Ohio','Colorado','Utah','New York']
               ,columns=['one','two','three','four'])

print(data)
# print(data[['three','one']])#获取多列
print(data['one'])
print(data[:2])#通过切片或者data[[2]]来访问