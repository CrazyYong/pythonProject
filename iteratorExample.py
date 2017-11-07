#!/usr/bin/python3
#coding=utf-8



#迭代器

'''
对于list、string、tuple、dict等这些容器对象,使用for循环遍历是很方便的。在后台for语句对容器对象调用iter()函数。
iter()是python内置函数。
iter()函数会返回一个定义了next()方法的迭代器对象，它在容器中逐个访问容器内的元素。
next()也是python内置函数。在没有后续元素时，next()会抛出一个StopIteration异常，通知for语句循环结束。

迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数的时候，迭代器会向我们返回它所记录位置的下一个位置的数据。
实际上，在使用next()函数的时候，调用的就是迭代器对象的_next_方法（Python3中是对象的_next_方法，Python2中是对象的next()方法）。
所以，我们要想构造一个迭代器，就要实现它的_next_方法。但这还不够，python要求迭代器本身也是可迭代的，
所以我们还要为迭代器实现_iter_方法，而_iter_方法要返回一个迭代器，
迭代器自身正是一个迭代器，
所以迭代器的_iter_方法返回自身self即可。

其实，当我们使用for语句的时候，for语句就会自动的通过__iter__()方法来获得迭代器对象，并且通过next()方法来获取下一个元素。
'''


listArray = [1,2,3]
iterName = iter(listArray)
for i in range(0,len(listArray)):
    print  next(iterName)
# print (iterName)
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))


#生成器
'''
延迟操作。也就是在需要的时候才产生结果，不是立即产生结果。
>生成器是只能遍历一次的。
>生成器是一类特殊的迭代器。

第一类：生成器函数：还是使用 def 定义函数，但是，使用yield而不是return语句返回结果。
yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行。
'''

'''
简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，
每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，
代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
'''

# 菲波那切数列
def Fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

f=Fib(10)
print (f.next())

##如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
from inspect import isgeneratorfunction
print (isgeneratorfunction(Fib) )


# while  True:
#     try:
#         x=next(f)
#         print("f:",x)
#     except StopIteration as e:
#         print("生成器最后的返回值是：",e.value)
#         break
'''
第二类：生成器表达式：类似于列表推导，只不过是把一对大括号[]变换为一对小括号()。
但是，生成器表达式是按需产生一个生成器结果对象，要想拿到每一个元素，就需要循环遍历。
'''
xiaoke=[2,3,4,5]
# 生成器generator，类似于list，但是是把[]改为()
gen=(a for a  in xiaoke)
for  i  in gen:
    print(i)
# 为什么要使用生成器？因为效率。
# 使用生成器表达式取代列表推导式可以同时节省 cpu 和 内存(RAM)。
# 如果你构造一个列表(list)的目的仅仅是传递给别的函数,
# 比如 传递给tuple()或者set(), 那就用生成器表达式替代吧!

# 本案例是直接把列表转化为元组
kk=tuple(a for a in xiaoke)
print(kk)
#结果是：
(2, 3, 4, 5)

# python内置的一些函数，可以识别这是生成器表达式，外面有一对小括号，就是生成器
result1=sum(a for a in range(4))
print(result1)
# 列表推导式
result2=sum([a for a in range(3)])
print(result2)

