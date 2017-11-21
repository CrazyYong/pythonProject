'''
1.人力资源。创建一个简单的雇员姓名和编号的程序。让用户输入一组雇员姓名和编号。
你的程序可以提供按照姓名排序输出的功能，雇员姓名显示在前面，后面是对应的雇员编号。
附加题：添加一项功能，按照雇员编号的顺序输出数据。
'''

import re
# number=re.sub("\D", "", input_tx)
# name=input_tx.split(number)[0]

# input_name=input('请输入一组姓名并以逗号分隔')
# name_list=input_name.split(',')
# input_number=input('请输入一组对应姓名编号并以逗号分隔')
# number_list=input_number.split(',')
# all_dict=dict(zip(name_list,number_list))
#
# print(sorted(all_dict.items(),key=lambda item:item[0]))


'''
2.以特殊方式跟管理员打招呼：创建一个至少包含5 个用户名的列表，且其中一
个用户名为'admin'。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。
遍历用户名列表，并向每位用户打印一条问候消息。
 如果用户名为'admin'，就打印一条特殊的问候消息，如“Hello admin, would you
like to see a status report?”。
 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
'''
# admin_list=['admin','emoply','bob','xiaowang','xiaolan']
#
# def hello_admin(name):
#     for i in range(0,len(admin_list)):
#         if admin_list[i]==name=='admin':
#             print('Hello admin, would you like to see a status report?')
#             break
#         elif name in admin_list:
#             print('Hello %s, thank you for logging in again'%name)
#             break
#         else:
#             print('你不是管理员，滚犊子')
#             break
#
#
# hello_admin('admin')
# hello_admin('bob')
# hello_admin('hhhh')

'''
3.处理没有用户的情形：在为完成练习2编写的程序中，添加一条if 语句，检
查用户名列表是否为空。
 如果为空，就打印消息“We need to find some users!”。
 删除列表中的所有用户名，确定将打印正确的消息。
'''
# admin_list=['admin']
#
# def hello_admin():
#     if len(admin_list)!=0:
#      for i in range(0,len(admin_list)):
#          if admin_list[i]=='admin':
#              print('Hello admin, would you like to see a status report?')
#          else :
#              print('Hello %s, thank you for logging in again'%(admin_list[i]))
#     else:
#         print('We need to find some users!')
#
# hello_admin()

'''
4.检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名
都独一无二的方式。
 创建一个至少包含5 个用户名的列表，并将其命名为current_users。
 再创建一个包含5 个用户名的列表，将其命名为new_users，并确保其中有一两
个用户名也包含在列表current_users 中。
 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是
这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指
出这个用户名未被使用。 
'''
current_users=['admin','emoply','bob','xiaowang','xiaolan']
new_users=['admin','feifei','bob','blany','join']

for i in range(0,len(new_users)):
        if new_users[i]==current_users[i]:
            print('%s该用户名已被使用，请输入其他用户名'%(new_users[i]))
        else:
            print('%s这个用户名可以使用'%(new_users[i]))
