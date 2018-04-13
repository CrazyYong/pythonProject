# -*- conding:UTF-8 -*-
# 1.在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python 知识，其中每一行都以
# “In Python you can”打头。将这个文件命名为learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。
# 编写一个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；第二次打印时遍历文件对象；
# 第三次打印时将各行存储在一个列表中。
#
for i in range(3):
    if i==0:
        with open('learning_python.txt','r',encoding='utf-8') as file:
           contents=file.read()
           print('第一遍')
           print(contents)
    elif i==1:
        with open('learning_python.txt', 'r', encoding='utf-8') as file:
            print('第二遍')
            for line  in file:
                print(line)
    elif i==2:
        with open('learning_python.txt', 'r', encoding='utf-8') as file:
            contents = file.readlines()
            print(contents)

# 2.下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'：
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# 读取你刚创建的文件learning_python.txt 中的每一行，将其中的Python 都替换为另
# 一门语言的名称，如C。将修改后的各行都打印到屏幕上。块外打印它们。
#r+中,替换内容相当于追加内容,
# with open('learning_python.txt','r+',encoding='utf-8') as file:
#     contents=file.read()
#     file.write(contents.replace('python','C'))
#     file.flush()
#     file.seek(0)
#     contents_1 = file.read()
#     print(contents_1)


# file1=open('learning_python.txt','r+',encoding='utf-8')
# content_1=file1.read()
# file1.close()
# file2=open('learning_python_1.txt','w+',encoding='utf-8')
# file2.write(content_1.replace('python','C'))
# file2.flush()
# file2.seek(0)
# cc=file2.read()
# print(cc)
# file2.close()

# 3.访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
# 入到文件guest.txt 中。
# while True:
#     name=input('请输入你的姓名:')
#     print('欢迎光临%s'%name)
#     if name=='q':
#         break
#     with open('guest.txt','a+',encoding='utf-8') as file:
#         file.write(name)
#         file.write('\n')
#         file.flush()
#         file.seek(0)
#         cc=file.read()
#         print(cc)

#异常
# try:
#     file=open('yichang.txt','r',encoding='utf-8')
# except FileNotFoundError:
#     print('sorry,这个文件不存在')
#
# try:
#     print(mm)
# except (FileNotFoundError,NameError):
#     print('sorry,这个文件不存在')
# except NameError:
#     print('亲爱的,你这个变量不存在!')

#除法运算简单计算器
# while 1:
#     try:
#         a=input('请输入第一个数:')
#         b=input('请输入第二个数:')
#         m=int(a)/int(b)
#
#     except ZeroDivisionError:
#         print('您输错了,请重新输入一遍!')
#         continue
#     else:
#         print(m)
#         break
#     finally:
#         print('不管你有没有错误,我都会执行!')

#异常题目
#
# 1 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
# 在这种情况下，当你尝试将输入转换为整数时，将引发TypeError 异常。编写一个程序，提示用户输入两个数字，
# 再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
# while 1:
#     try:
#         a=int(input('请输入第一个数:'))
#         b=int(input('请输入第二个数:'))
#     except ValueError:
#         print('你输入不是整数,是字符串')
#         continue
#     else:
#         print(a+b)
#         break


# 3 猫和狗：创建两个文件cats.txt 和dogs.txt，在第一个文件中至少存储三只猫的名字，
# 在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。

def find_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as file:
            cc=file.read()
            print(cc)
    except FileNotFoundError:
        # pass
        print('亲爱的,您的文件不存在')
    else:
        print('打印出来啦')

find_file('cats.txt')