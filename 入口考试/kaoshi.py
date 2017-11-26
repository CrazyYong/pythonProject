'''
2：输入一个文件名，如果不存在，创建。打开文件，输入写入文件。输入“#”就结束输入，打印文件内容。退出程序。
如果写入报错，直接关闭文件退出程序

'''

# while True:
#     txt=input('请输入#号')
#     if txt=='#':
#         with open('czy.txt','w+',encoding='utf-8') as file:
#             try:
#                 file.write(txt)
#                 file.write('\n')
#                 file.flush()
#                 file.seek(0)
#                 txt_read = file.read()
#                 print (txt_read)
#                 break
#             except FileNotFound:
#                 file.close
#                 break
bc
'''
3.输入不少于五个数字，数字之间以空格分为界。然后将这些数字排序，不能用内置函数
'''

input_txt=input('请输入不少于五个数字，数字之间用空格隔开')
list_num=input_txt.split(' ')

array = [int(x) for x in list_num]
for i in range(len(array))[::-1]:
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print (array)


'''
4.[1,1,0,2,2,2,3,4,0,0,1,1]将连续相同项保存在一起，添加至一个列表中。
最后输出[[1,1],[0],[2,2,2],[3],[4],[0,0],[1,1]] 用函数形式表示出来
'''

# lists=[1,1,0,2,2,2,3,4,0,0,1,1]
# list1=lists[0:2]
# list2=lists[2:3]
# list3=lists[3:6]
# list4=lists[6:7]
# list5=lists[7:8]
# list6=lists[8:10]
# list7=lists[10:12]
# list_a=[]
# list_a.insert(0,list1)
# list_a.insert(1,list2)
# list_a.insert(2,list3)
# list_a.insert(3,list4)
# list_a.insert(4,list5)
# list_a.insert(5,list6)
# list_a.insert(6,list7)
# print (list_a)


'''
小明和女朋友买了一堆士力架，先是女朋友吃了一半，然后小明又吃了一个，第二天他女朋友吃了一半
，然后小明吃了一个，直到第六天只剩下一个，问小明到底买了多少士力架
'''

