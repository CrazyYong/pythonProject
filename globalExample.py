#!/usr/bin/python3
#coding=utf-8

#global全局变量

#用global之后就可以修改外面的变量
a='6'
def fun():
    global a
    a = '7'
    print (a)

fun()
print (a)


#如果不用，那么修改的只是内部的变量跟外部的变量没关系
def func_local(x):
    print ('x is', x)
    x = 2
    print ('Chanaged local x to',x)

x = 50
func_local(x)
print ('x is still', x)

#函数参数若是list、set、dict可变参数，在函数内改变参数，会导致该参数发生变化，例如：
#(1)
def func_local(x):
    print ('x is', x)
    x.append(10)
    print ('Chanaged local x to',x)

x = range(6)
func_local(x)
print ('x is', x)
#(2)
def func_local(x):
    print ('x is', x)
    x.add(10)
    print ('Chanaged local x to',x)

x = set(range(6))
func_local(x)
print ('x is', x)
#(3)
def func_local(x):
    print ('x is', x)
    x.add(10)
    print ('Chanaged local x to',x)

x = set(range(6))
func_local(x)
print ('x is', x)
#如果是元组的话，就不行了，改变不了外面的
def func_local(x):
    print ('x is', x)
    x = (4, 5, 6)
    print ('Chanaged local x to',x)

x = (1,2,3,)
func_local(x)
print ('x is', x)

