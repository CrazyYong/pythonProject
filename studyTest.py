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
# for i in range(1,9,2):
#     m=i*'*'
#     print(m.center(7))
# while i <=7 and i>1:
#     i-=2
#     m = i * '*'
#     print(m.center(7))


#7. 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
#     例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
# for i in range(100,1000):
#     #首先分解百数 比如153
#     x=i//100
#     # 首先分解十数 比如153
#     y=i%100//10
#     # 首先分解个数 比如153
#     z=i%100%10
#     if i == x**3+y**3+z**3:
#         print(i)
#列表推导式
# list1=[i for i in range(100,1000) if i == (i//100)**3+(i%100//10)**3+(i%100%10)**3 ]
# print(list1)

#8.求M,N中矩阵对应元素的和元素的乘积
# m = [[1,2,3],[4,5,6],[7,8,9]]
# n = [[2,2,2],[3,3,3],[4,4,4]] 求两个列表对应元素的积
# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# n = [[2,2,2],
#      [3,3,3],
#      [4,4,4]]
#
# ji=[m[i][j]*n[i][j] for i in range(3) for j in range(3)]
# print(ji)

#9.假设一个简单的ATM机的取款过程是这样的：
'''
首先提示用户输入密码，最多只能输入三次，超过三次则提示用户“密码错误，请取卡”结束交易
。如果用户密码正确，再提示用户输入金额。ATM机只能输出100元的纸币，一次取钱要求最低0元，
最高1000元。如果用户输入的金额符合上述要求。则打印出用户取得钱数，最后提示用户“交易完成
，请取卡”，否则提示用户重新输入金额
假设密码是 888888
'''
# password_correct='888888'
# password_num=0
# while True:
#     password_txt=input('请输入密码')
#     if password_txt==password_correct:
#         money_txt=input('请输入金额，最大面额100元，最低取0元，最高1000元:')
#         if int(money_txt)%100==0 and int(money_txt)>=0 and int(money_txt)<=1000:
#             new_txt=input('您的取得金额是%s'%money_txt+'\n'+"回复Y继续取钱，回复N请取卡:")
#             if new_txt=='Y':
#                 continue
#             else:
#                 break
#
#     elif password_num<3:
#         password_num+=1
#         print(password_num)
#         print('密码输入错误，请重新输入')
#         continue
#     elif password_num>=3:
#         print('密码输入错误超过，结束交易')
#         break



# 10.将列表用for循环添加到另一个字典中.
# mm=['dog','cat','people','name']
# # list1=list(enumerate(mm))
# # print(list1)
# nn=[0,1,2,3]
# ll={key:value  for key,value in enumerate(mm)}
# print(ll)


# 11.编写一个函数，输入n为偶数时，调用函数1/2+1/4+...+1/n，当输入为奇数时，调用函数
# 1/1+1/3+...+1/n
# 1-1/2+1/2-1/4+1/4-1/8.2/n-1/n=1-1/n=（n-1）/n

mm = int(input('请输入一个数'))
if mm % 2 == 0:
    # event_num=(mm-1)/mm
    print ('%d/%d' % (mm - 1, mm))
elif mm % 2 == 1:
    for i in range(1, mm + 2, 2):
        sum += 1.0 / i
        print (sum)




