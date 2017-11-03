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

