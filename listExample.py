#!/usr/bin/python3
#coding=utf-8

#列表List


'''
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
'''
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];


##访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

##更新列表
lists = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print lists[2];
lists[2] = 2001;
print "New value available at index 2 : "
print lists[2];

##删除列表元素
list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

##Python列表脚本操作符
##列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
print len([1,2,3]) ##长度
print [1, 2, 3] + [4, 5, 6] ##组合
print ['Hi!'] * 4 ##重复
print 3 in [1, 2, 3] ##元素是否存在于列表
for x in [1, 2, 3]: print x ##迭代

##Python列表截取
L = ['Google', 'Runoob', 'Taobao']
print L[2]
print L[-2] ##读取列表中倒数第二个元素
print L[1:] ##从第二个元素开始截取列表

##Python列表函数&方法

###cmp() 方法用于比较两个列表的元素。
'''
返回值
如果比较的元素是同类型的,则比较其值,返回结果。
如果两个元素不是同一种类型,则检查它们是否是数字。
如果是数字,执行必要的数字强制类型转换,然后比较。
如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
否则,通过类型名字的字母顺序进行比较。
如果有一个列表首先到达末尾,则另一个长一点的列表"大"。
如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
'''
list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
print cmp(list2, list3)
###len() 方法返回列表元素个数。
list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print "First list length : ", len(list1);
print "Second list length : ", len(list2);
###max() 方法返回列表元素中的最大值。
list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print "Max value element : ", max(list1);
print "Max value element : ", max(list2);
###min() 方法返回列表元素中的最小值。
list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print "min value element : ", min(list1);
print "min value element : ", min(list2);
###list() 方法用于将元组转换为列表。
###注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)

print "列表元素 : ", aList
###append() 方法用于在列表末尾添加新的对象。
aLists = [123, 'xyz', 'zara', 'abcc'];
aLists.append( 2009 );
print "Updated List : ", aLists;
###count() 方法用于统计某个元素在列表中出现的次数。
aList = [123, 'xyz', 'zara', 'abc', 123];

print "Count for 123 : ", aList.count(123);
print "Count for zara : ", aList.count('zara');
###extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)

print "Extended List : ", aList ;
###index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
aList = [123, 'xyz', 'zara', 'abc'];

print "Index for xyz : ", aList.index( 'xyz' ) ;
print "Index for zara : ", aList.index( 'zara' ) ;
###insert() 函数用于将指定对象插入列表的指定位置。
aList = [123, 'xyz', 'zara', 'abc']

aList.insert(3, 2009)

print "Final List : ", aList
###pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
aList = [123, 'xyz', 'zara', 'abc'];

print "A List : ", aList.pop();
print "B List : ", aList.pop(2);
###remove() 函数用于移除列表中某个值的第一个匹配项。
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.remove('xyz');
print "List : ", aList;
aList.remove('abc');
print "List : ", aList;
###reverse() 函数用于反向列表中元素
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.reverse();
print "List : ", aList;
###sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.sort();
print "List : ", aList;




'''
列表推导式
和列表一样，列表推导式也采用了方括号[]，并且用到了一个简写版的for循环，第一部分是一个
生成结果列表元素的表达式，第二部分是一个输入表达式的循环。
阅读理解列表表达式的推荐做法是先从里面的for循环开始，向右查看是否有if条件，然后推导式
开始的那个表达式映射到每一个匹配的元素上去
'''
lis1=[1,2,3,4,5]
list2=[x for x in lis1 if x>3]
print (list2)

'''
求（x,y）其中x是0-5之间的偶数，y是0-5之间的奇数组成的元组列表
'''
new_list=[(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1]
print (new_list)



list1=[i for i in range(100,1000) if i == (i//100)**3+(i%100//10)**3+(i%100%10)**3 ]
print(list1)


#镶嵌列表推导式

names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
list1=[name.lower()  for lis in names for name in lis if name.count('e')>=2 ]
print(list1)

