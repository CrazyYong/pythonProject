#!/usr/bin/python3
#coding=utf-8

import math


'''
题目:
1.有一个列表a[],里面有若干个整数未知,希望将里面的整数两两做差,即a[1]-a[0],a[3]-a[2]..,
并将得数保存在另一个列表b[]中,请问如何实现?
'''
# list1=[]
# list2=[]
# while True:
#     inputTxt=input('请输入一个数字')
#     if inputTxt=='n':
#         break
#     if inputTxt.isalpha():
#         continue
#     list2.append(int(inputTxt))
# for i in range(0,len(list2)-1):
#     j=list2[i+1]-list2[1]
#     list1.append(j)
# print(list1)


'''
2.从键盘输入一个字符串，将小写字母全部转换成大写字母，将字符串以列表的形式输出
（如果字符串包含整数，并取整）
'''
# mm=input("请输入字符串")
# list3=list(mm)
# numList=[]
# abcList=[]
# for i in range(0,len(list3)-1):
#     j= list3[i]
#     if j.isnumeric():
#         numList.append(j)
#     else:
#         abcList.append(j.upper())
# print(numList,abcList)

'''
3.随机输入8位的正整数，要求：一、求它是几位数，二、逆序打印出个位数字
'''
# mm=input('请输入整数')
# print(str(len(mm))+'位')
# newList=list(mm)
# newList.reverse()
# print(newList)


'''
4.一球从n米（自己输入）高度自由落下，每次落地后反跳回原来高度的一半；再落下
，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

# aa = input("请输入高度")
# heathNum=int(aa)
# baHeath=heathNum;
# everyHeath=0
# toutalNum=heathNum
# lowHeath=0
# for i in range(1,11):
#     baHeath = baHeath/float(2)
#     print(baHeath)
#     toutalNum = toutalNum+baHeath
#     lowHeath=baHeath
# print(toutalNum*2-heathNum)
# print(lowHeath)

'''
5.输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
'''
# mm=input('请输入一串字符')
# list4=list(mm)
# enNum = 0
# balckNum = 0
# numNum = 0
# otherNum=0
# for i in range(0,len(list4)-1):
#     j=list4[i]
#     if j.isnumeric():
#         numNum=numNum+1
#     elif j.isalpha():
#         enNum=enNum+1
#     elif j=="\000":
#         balckNum=balckNum+1
#     else:
#         otherNum=otherNum+1
# print(enNum,balckNum,otherNum,numNum)



#6..打印出如下图案（菱形）
#  
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
for i in range(1,9,2):
    m=i*'*'
    print(m.center(7))
while i <=7 and i>1:
    i-=2
    m = i * '*'
    print(m.center(7))


#7. 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
#     例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
for i in range(100,1000):
    #首先分解百数 比如153
    x=i//100
    # 首先分解十数 比如153
    y=i%100//10
    # 首先分解个数 比如153
    z=i%100%10
    if i == x**3+y**3+z**3:
        print(i)
#列表推导式
list1=[i for i in range(100,1000) if i == (i//100)**3+(i%100//10)**3+(i%100%10)**3 ]
print(list1)

#8.求M,N中矩阵对应元素的和元素的乘积
# m = [[1,2,3],[4,5,6],[7,8,9]]
# n = [[2,2,2],[3,3,3],[4,4,4]] 求两个列表对应元素的积
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
n = [[2,2,2],
     [3,3,3],
     [4,4,4]]

ji=[m[i][j]*n[i][j] for i in range(3) for j in range(3)]
print(ji)

