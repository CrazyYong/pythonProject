'''
1.求1-2+3-4+5 ... 99的所有数的和
'''

# sum=0
# for i in  range(1,100):
#     sum=sum+i;
#
# print(sum)


'''
2.写代码，有如下变量，请按照要求实现每个功能

name = " aleX "

a.移除name变量对应的值两边的空格，并输入移除有的内容
b.判断name变量对应的值是否以 "al"开头，并输出结果
c.判断name变量对应的值是否以 "X"结尾，并输出结果
d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
e.将name变量对应的值根据 " l" 分割，并输出结果。
f.请问，上一题 e分割之后得到值是什么类型？ 字符串
g.将name变量对应的值变大写，并输出结果
h.将name变量对应的值变小写，并输出结果
i.请输出name变量对应的值的第2个字符？
j.请输出name变量对应的值的前3个字符？
k.请输出name变量对应的值的后2个字符？
l.请输出name变量对应的值中 "e" 所在索引位置？

'''
name=' aleX '
print(name.strip(' '))
print(name.startswith('al'))
print(name.endswith('X'))
print(name.replace('l','p'))
print(name.split('l'))
print(name.upper())
print(name.lower())
print(name[2])
print(name[3])
print(name[3:5])
list1=list(name)
print(list1)
print(list1.index('e'))

'''
3.写代码，有如下列表，按照要求实现每一个功能（练习题同样适用于元组）

li = ['alex','eric','rain']    
a.计算列表长度并输出
b.列表中追加元素"seven"，并输出添加后的列表
c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
e.请删除列表中的元素"eric"，并输出修改后的列表
f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
g.请删除列表中的第3个元素，并输出删除元素后的列表
h.请删除列表中的第2至4个元素，并输出删除元素后的列表
i.请将列表所有的元素反转，并输出反转后的列表
j.请使用for、len、range 输出列表的索引
k.请使用enumrate输出列表元素和序号（序号从 100 开始）
l.请使用for循环输出列表的所有元素
'''

li=['alex','eric','rain']
print('列表长度%d'%(len(li)))
li.insert(0,'Tony')
print(li)
li.append('seven')
print(li)
li.insert(1,'Kelly')
print(li)
li.remove('eric')
print(li)
print(li.pop(2))
print(li)
print(li.pop(3))
print(li)



li = ['alex', 'eric', 'rain','Tony']
for i in range(3):
    li.pop(1)
print(li)


l = ['alex', 'eric', 'rain','Tony']
print(l.reverse())

li = ['alex', 'eric', 'rain','Tony']
for i in range(len(li)):
    print(i)


l = ['alex', 'eric', 'rain','Tony']
for i,name in enumerate(li):
    print(i,name)

for i in range (len(l)):
    print(l[i])


'''
4.有如下变量，请实现要求的功能
tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
a. 讲述元祖的特性
b. 请问 tu 变量中的第一个元素 "alex" 是否可被修改？
c. 请问 tu 变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
d. 请问 tu 变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
'''
'''
a.不可修改
b.不可以修改
c列表
d元组，不可以
'''
tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])

li=tu[1]
print(li)

lli=li[2]
print(lli)

llli=lli['k2']
llli.append('Seven')
print(llli)

tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
b = list(tu[1][2]["k3"])#k3的value转换list
b.append("seven")#添加值
tu[1][2]["k3"] = tuple(b)#给k3赋值
print(tu)


'''
5.字典
dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
a. 请循环输出所有的 key
b. 请循环输出所有的 value
c. 请循环输出所有的 key 和 value
d. 请在字典中添加一个键值对， "k4":"v4"，输出添加后的字典
e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
f. 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
g. 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典
'''

dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
for i in dic.keys():
    print(i)

for i in dic.keys():
    print(dic.get(i))

for i in dic.items():
    print(i)

dic['k4']='v4'
print(dic)

dic['k1']='alex'
print(dic)

l=dic.get('k3')
l.append(44)
print(dic)

l=dic.get('k3')
l.insert(0,18)
print(dic)





