#!/usr/bin/python3
#coding=utf-8




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
从键盘输入一个字符串，将小写字母全部转换成大写字母，将字符串以列表的形式输出
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
随机输入8位的正整数，要求：一、求它是几位数，二、逆序打印出个位数字
'''
# mm=input('请输入整数')
# print(str(len(mm))+'位')
# newList=list(mm)
# newList.reverse()
# print(newList)


'''
一球从n米（自己输入）高度自由落下，每次落地后反跳回原来高度的一半；再落下
，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

aa = input("请输入高度")
heathNum=int(aa)
baHeath=heathNum;
everyHeath=0
toutalNum=heathNum
lowHeath=0
for i in range(1,11):
    baHeath = baHeath/2
    print(baHeath)
    toutalNum = toutalNum+baHeath
    lowHeath=baHeath
print(toutalNum)
print(lowHeath)


'''
输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
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








# di2={}
# for i in range(0,3):
#     key=input('输入一个键');
#     value=input('输入一个值')
#     di1={key:value}
#     di2.update(di1)
# print di2

##原码补码 反码

