#!/usr/bin/python3
#coding=utf-8




#Python 标识符
'''
在 Python 里，标识符由字母、数字、下划线组成。
在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
Python 中的标识符是区分大小写的。
以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
Python 可以同一行显示多条语句，方法是用分号 ; 分开，如：

'''

print ('hello');print ('runoob');








#Python注释
# 第一个注释
print ("Hello, Python!");  # 第二个注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""


#等待用户输入
a=input("\n\nPress the enter key to exit.")


#同一行显示多条语句，Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n')



#Python 引号
#Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
#其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""


#多行语句
#Python语句中一般以新行作为为语句的结束符。
#但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
total = 'item_one' + \
        'item_two' + \
        'item_three'
#语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']