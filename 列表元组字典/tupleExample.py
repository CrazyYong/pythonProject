#!/usr/bin/python3
#coding=utf-8

#元组tuple
'''
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
'''
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

tup1 = ();##创建空元组
tup1 = (50,);#元组中只包含一个元素时，需要在元素后面添加逗号

##访问元组
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

##修改元组
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

### 以下修改元组元素操作是非法的。
### tup1[0] = 100;

### 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)

##删除元组
##元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，删除后再打印会报错，如下实例:
# tup = ('physics', 'chemistry', 1997, 2000);
#
# print tup;
# del tup;
# print "After deleting tup : "
# print tup;

##元组运算符(和列表一样，查看列表代码)

##元组索引，截取(和列表一样，查看列表代码)

##无关闭分隔符
##任意无符号的对象，以逗号隔开，默认为元组，如下实例：
print ('abc', -4.24e93, 18+6.6j, 'xyz');
x, y = 1, 2;
print ("Value of x , y : ", x,y);

##元组内置函数(cmp(),len(),max(),min()方法和列表类似)
###tuple() 函数将列表转换为元组。
print (tuple([1,2,3,4]))
print (tuple({1:2,3:4})) ###针对字典 会返回字典的key组成的tuple
print (tuple((1,2,3,4))) ###元组会返回元组自身

#元组推导式

names = {'Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe','Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva'}
# list1={name.upper() for name in names if len(name)>=4}
# print(list1)
list2=(name.upper() for name in names if len(name)>=5)
list3=[name.upper() for name in names if len(name)>=5]
m=iter(list2) #用iter函数生成迭代器对象
print(list3)
print(next(m))#用next去遍历其中的值 yield
print(next(m))#用next去遍历其中的值 yield
print(next(m))#用next去遍历其中的值 yield