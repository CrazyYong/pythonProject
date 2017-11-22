#!/usr/bin/python3
#coding=utf-8


#内置函数

##dict() 函数用于创建一个字典。
'''
语法
dict 语法：
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
参数说明：
**kwargs -- 关键字
mapping -- 元素的容器。
iterable -- 可迭代对象。
'''
print (dict())
print (dict(a='a', b='b', t='t'))
print (dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print (dict([('one', 1), ('two', 2), ('three', 3)]))

##divmod() 函数
'''
divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
在 python 2.3 版本之前不允许处理复数。
'''
print (divmod(7, 2))
print (divmod(1+2j,1+0.5j))

##range() 函数用法
'''
 range() 函数可创建一个整数列表，一般用在 for 循环中。
 
 range(start, stop[, step])
 参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
end: 计数到 end 结束，但不包括 end。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
print (range(10))
print (range(1,11))
print (range(0,30,5))

##all()函数
'''
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。
注意：空元组、空列表返回值为True，这里要特别注意。
'''
b=all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
print (b)

b=all([0,1,2,3])      # 列表list，存在一个为0的元素
print (b)

b=all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
print (b)

b=all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
print (b)

b=all((0, 1,2, 3))          # 元组tuple，存在一个为0的元素
print (b)

print (all([]))             #空列表

print (all(()))             #空元组

##filter()函数
'''
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中
'''
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
##也可以使用lambda表达式
print (filter(lambda x:x>3,[1,2,3,4]))


##map()函数
'''
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
参数
function -- 函数，有两个参数
iterable -- 一个或多个序列
'''
def sequare(x):
    return x ** 2

print (map(sequare,[1,2,3,4]))


##reduce() 函数
'''
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
'''
# def add(x,y):
#     return x+y
# print (reduce(add, [1,2,3,4,5]) )
