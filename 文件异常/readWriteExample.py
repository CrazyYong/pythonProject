#!/usr/bin/python3
#coding=utf-8

# with open('Python.txt','r') as ff:
#     contents=ff.read()
#     print(contents)

#用open结合for循环逐行打印
# ff =open('Python.txt','r')
# #readlines读取到的内容形成列表
# i=1
# for line  in ff:
#     print('这是第%d行,内容是%s'%(i,line))
#     i+=1

#with open 逐行读取1
# with open('Python.txt','r') as file:
#     i=1
#     for line in file:
#         print('这是第%d行,内容是%s' % (i, line))
#         i+=1

#open结合readlines逐行打印,并返回行数
# ff =open('Python.txt','r')
# #readlines读取到的内容形成列表
# contens=ff.readlines()
# ff.close()
# i=1
# for line  in contens:
#     print('这是第%d行,内容是%s'%(i,line),end='')
#     i+=1

#with open 结合readlines
# with open('Python.txt','r') as file:
#     lines=file.readlines()
#     i=1
#     for line in lines:
#         print('这是第%d行,内容是%s' % (i, line))
#         i+=1


#with open 写入文件
with open('lala.txt','a') as file:
    file.write(r'I love Python\n')
    file.close()

# with open('lala.txt', 'r') as file:
#     contents=file.read()
#     print(contents)