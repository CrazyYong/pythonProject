'''
1.给定一个整数N，判断N是否为质数（10分）
'''
# 用户输入数字
# num = int(input("请输入一个数字: "))
#
# # 质数大于 1
# if num > 1:
#     # 查看因子
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "不是质数")
#             print(i, "乘于", num // i, "是", num)
#             break
#     else:
#         print(num, "是质数")
#
# # 如果输入的数字小于或等于 1，不是质数
# else:
#     print(num, "不是质数")

'''
2、实现用户输入用户名和，密码，当用户名为 joe 且 密码为 123456 时，显示登陆成功否则登陆失败，失败时允许重复输入三次（10分）（10）
'''
# name = input('请输入用户名')
# password = input('请输入密码')
# num = 0
# while True:
#     num += 1
#     if num<3:
#         if name=='joe' and password=='123456':
#             print('登录成功')
#             break
#         else:
#
#             print('用户名或密码错误请重新输入')
#             name = input('请输入用户名')
#             password = input('请输入密码')
#             continue
#     else:
#         print('您输入的次数超过三次')
#         break

'''
3、随意输入三个整数x,y,z，输出其中的最大者。（10分）；
'''
# num =input("请输入三个数字并以空格分开")
# number_list=num.split(' ')
# print(max(number_list))


'''
4、一群猴子排成一圈，按1，2，...，n依次编号。然后从第1只开始数，数到第m只,把它踢出圈，
从它后面再开始数，再数到第m只，在把它踢出去...，如此不停的进行下去，
直到最后只剩下一只猴子为止，那只猴子就叫做大王。要求编程模拟此过程，输出最后那个大王。（10）
'''
# def yuese(n,k):
#     index=0
#     #针对n个人形成一个列表
#     people=list(range(1,n+1))
#     while 1:
#         if len(people)==2:
#             break
#         #index是删除的索引值
#         index=(index+(k-1))%len(people)
#         del people[index]
#     print('存活下来的两个幸运的人',people)
# mm= yuese(45,3)

'''
5、有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？用程序实现（10分）
'''
'''
6、有一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入列表中。（10分）
例：[1,3,4,6]   输入一个数：5  结果：[1,3,4,5,6]
'''

#
# i = int(input('请输入一个数字:'))
#
# li = [1,3,4,6,7]
#
# print(li)
#
# for x in range(5):
#
#     if i <= li[0]:
#         li.insert(0, i)
#         break
#     elif i >= li[4]:
#         li.append(i)
#         break
#     elif i > li[x] and i <= li[x + 1]:
#         li.insert(x + 1, i)
#         break
#
# print(li)

'''
7、关于列表、元祖、字典基本操作（20分）
（1）给出以下两个列表
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7, (1, 2, 3, ['hate', 'python'])]
请分别完成如下操作：
（1）for循环输出列表内容
（2）更新列表2的hate为love
（3）两种方式删除列表1中值为2000的数据
（4）列表2中在下标为0处插入元素为”hello beifeng”的数据。
（2）关于元组
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 3, 3)
请分别完成如下操作：
（1）遍历输出元组内容
（2）更新tup1的1997为2016
（3）删除tup2中值为5的数据
（4）元组2中插入值为”hello beifeng”的数据
（5）统计元组2中3在元组中出现的次数
（6）遍历tup1与tup2合并后的元组。
（3）关于字典：编写程序建立空字典，循环依次输入下列键值对，每输入一次，询问是否继续，如果不在继续输入，则分别打印刚刚输入字典的键和值。
'''




# list1 = ['physics', 'chemistry', 1997, 2000];
# list2 = [1, 2, 3, 4, 5, 6, 7, (1, 2, 3, ['hate', 'python'])]
#
# for i in list1:
#     print(i)
#
# for i in list2:
#     print(i)
#
# tup=list2[7]
# list3=tup[3]
# list3[0]='love'
# print(list3)

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7, (1, 2, 3, ['hate', 'python'])]

# list1.remove(2000)
# print(list1)

# list1.pop(3)
# print(list1)
#
#
# list2.insert(0,'hello beifeng')
# print(list2)

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 3, 3)

# for i in tup1:
#     print(i)
#
# for i in tup2:
#     print(i)
#
# list1=list(tup1)
# print(list1)
#
# list1[2]=2016
# print(list1)
# tup1=tuple(list1)
# print(tup1)

sum=0
for i in tup2:
    if i==3:
        sum+=1
print(sum)


tup3=tup1+tup2

for i in tup3:
    print(i)

