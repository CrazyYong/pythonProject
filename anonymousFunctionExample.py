#!/usr/bin/python3
#coding=utf-8


#匿名函数
#lambda表达式
#lambda argument1,argument2,...argumentN:expression using arguments

print (filter(lambda x:x>3,[1,2,3,4]))


#带参数匿名函数
a=(lambda x:x*3)
b=(lambda x,y:x+y)
print (a(3))
print (b(3,4))


#无参数匿名函数
t =  lambda :True
print (t())

#匿名函数调用
c=lambda x,y,z:x*y*z
print (c(3,2,4))

c=(lambda x,y=2:x*3)#使用了默认值
print (c(10))

a = lambda *z:z #*z返回的是一个元祖
print (a('Testing1','Testing2'))

c = lambda **Arg: Arg #arg返回的是一个字典
print (c())

print ((lambda x,y: x if x> y else y)(101,102))#直接后面传递实参
print ((lambda x:x**2)(3))


a=filter(lambda x:x%3==0,[1,2,3,4,6]) #结合filter使用，
print (a)
#等价于下面的列表推导式
l=[x for x in [1,2,3,5,6] if x%3==0]
print (l)


#嵌套使用
#lambda嵌套到普通函数中,lambda函数本身做为return的值
#(1)
def increment(n):
    return lambda x: x+n
f=increment(4)
print (f(2))
#(2)
def say():
    title='Sir'
    action=lambda x:title+x
    return action
act=say()
print (act('Smith!'))

'''
大量例子
'''
#例01: 字符串联合，有默认值，也可以x=(lambda...)这种格式
x=(lambda x='Boo',y='Too',z='Zoo':x+y+z)
print (x('Foo'))

#例02: 和列表联合使用
L=[lambda x:x**2,\
   lambda x:x**3,\
   lambda x:x**4]
for f in L:
    print (f(2))

#例03: 和字典结合使用
key = 'B'
dic={'A':lambda:2*2,\
     'B':lambda :2*4,\
     'C':lambda :2*8}
print (dic[key]())

#例04: 求最小值
lower=lambda x,y:x if x<y else y
print (lower('aa','bb'))


#例05: map及list联合使用
import sys
showall = lambda x:list(map(sys.stdout.write,x))
print ((['Jerry\n','Sherry\n','Alice\n']))


#例06: 判断字符串是否以某个字母开头

print (lambda x: x.startswith('B'))('Bob')