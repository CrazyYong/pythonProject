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
def yuese(n,k):
    index=0
    #针对n个人形成一个列表
    people=list(range(1,n+1))
    while 1:
        if len(people)==2:
            break
        #index是删除的索引值
        index=(index+(k-1))%len(people)
        del people[index]
    print('存活下来的两个幸运的人',people)
mm= yuese(45,3)

'''
5、有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？用程序实现（10分）
'''
