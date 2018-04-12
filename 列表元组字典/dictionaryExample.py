#!/usr/bin/python3
#coding=utf-8

#字典
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

'''
#d = {key1 : value1, key2 : value2 }

'''
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
一个简单的字典实例：
'''
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
#也可如此创建字典：
dict1 = { 'abc': 456 };
dict2 = { 'abc': 123, 98.6: 37 };

##访问字典里的值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print ("dict['Name']: ", dict['Name']);
print ("dict['Age']: ", dict['Age']);

##修改字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8;  # update existing entry
dict['School'] = "DPS School";  # Add new entry

print ("dict['Age']: ", dict['Age']);
print ("dict['School']: ", dict['School']);

##删除字典元素 但这会引发一个异常，因为用del后字典不再存在：
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
#

# dict.clear();  # 清空词典所有条目
# del dict;  # 删除词典
#
# print "dict['Age']: ", dict['Age'];
# print "dict['School']: ", dict['School'];

##字典键的特性
'''
字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
'''
###1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};

print ("dict['Name']: ", dict['Name']);
###2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，用的话会报错，如下实例：
# dict = {['Name']: 'Zara', 'Age': 7};
#
# print "dict['Name']: ", dict['Name'];


##字典内置函数&方法

###cmp() 函数用于比较两个字典元素。
# dict1 = {'Name': 'Zara', 'Age': 7};
# dict2 = {'Name': 'Mahnaz', 'Age': 27};
# dict3 = {'Name': 'Abid', 'Age': 27};
# dict4 = {'Name': 'Zara', 'Age': 7};
# print ("Return Value : %d" %  cmp (dict1, dict2))
# print ("Return Value : %d" %  cmp (dict2, dict3))
# print ("Return Value : %d" %  cmp (dict1, dict4))

###字典(Dictionary) len() 函数计算字典元素个数，即键的总数。
dict = {'Name': 'Zara', 'Age': 7};
print ("Length : %d" % len (dict))

###字典(Dictionary) str() 函数将值转化为适于人阅读的形式，以可打印的字符串表示。
dict = {'Name': 'Zara', 'Age': 7};
print ("Equivalent String : %s" % str (dict))

###type() 函数返回输入的变量类型，如果变量是字典就返回字典类型。
dict = {'Name': 'Zara', 'Age': 7};
print ("Variable Type : %s" %  type (dict))

###clear() 函数用于删除字典内所有元素。
dict = {'Name': 'Zara', 'Age': 7};

print ("Start Len : %d" %  len(dict))
dict.clear()
print ("End Len : %d" %  len(dict))

###copy() 函数返回一个字典的浅复制。
dict1 = {'Name': 'Zara', 'Age': 7};

dict2 = dict1.copy()
print ("New Dictinary : %s" % str(dict2))
####直接赋值和 copy 的区别
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)

###fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
'''
语法
fromkeys()方法语法：
dict.fromkeys(seq[, value]))
参数
seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值。
'''
seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict))

###get() 函数返回指定键的值，如果值不在字典中返回默认值。
'''
语法
get()方法语法：
dict.get(key, default=None)
参数
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
'''
dict1 = {'Name': 'Zara', 'Age': 27}

print ("Value : %s" %  dict1.get('Age'))
print ("Value : %s" %  dict1.get('Sex', "Never"))

### in 用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
dict1 = {'Name': 'Zara', 'Age': 7}

print ("Value : %s" %('Age' in dict1))
print ("Value : %s" % ('HE' in dict1))

###items() 函数以列表返回可遍历的(键, 值) 元组数组。
dict1 = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print ("字典值 : %s" % dict1.items())

# 遍历字典列表
for key, values in dict.items():
    print (key, values)

###keys() 函数以列表返回一个字典所有的键。
dict1 = {'Name': 'Zara', 'Age': 7}

print ("Value : %s" %  dict1.keys())

### setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
'''
语法
setdefault()方法语法：
dict.setdefault(key, default=None)
参数
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
'''
dict1 = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

print ("Value : %s" % dict1.setdefault('runoob', None))
print ("Value : %s" % dict1.setdefault('Taobao', '淘宝'))

###update() 函数把字典dict2的键/值对更新到dict里。
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict1.update(dict2)
print ("Value : %s" %  dict1)

###values() 函数以列表返回字典中的所有值。
dict1 = {'Name': 'Zara', 'Age': 7}

print ("Value : %s" %  dict1.values())

###pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print (pop_obj)

###popitem() 方法随机返回并删除字典中的一对键和值。如果字典已经为空，却调用了此方法，就报出KeyError异常。
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)