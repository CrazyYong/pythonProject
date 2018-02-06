#!/usr/bin/python3
#coding=utf-8


#for循环

for letter in 'Python':
    print ('当前字母：',letter)


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 :', fruits[index])



for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')


#99乘法表 for 循环1*1=1
        # 2*1=2 2*2=4
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end=' ')
    print()
'''

