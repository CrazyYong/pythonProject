#!/usr/bin/python3
#coding=utf-8


#函数
'''

你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

'''


def functionname( parameters ):
   "函数_文档字符串"
   print (parameters)
   return '返回值'

print (functionname(5))

##参数传递  在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]

a="Runoob"
'''
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，
她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。
'''

##可更改(mutable)与不可更改(immutable)对象
'''
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，
不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''


##python 传不可变对象实例
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print b # 结果是 2
'''
实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，
在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
'''

##传可变对象实例
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist


##参数
'''
以下是调用函数时可使用的正式参数类型：
必备参数
关键字参数
默认参数
不定长参数
'''

###必备参数
'''
必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
调用printme()函数，你必须传入一个参数，不然会出现语法错误：
'''
# 可写函数说明
# def printme(str):
#     "打印任何传入的字符串"
#     print str;
#     return;
#
# # 调用printme函数,会报错，因为没有传参数
# printme();

##关键字参数
'''
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
以下实例在函数 printme() 调用时使用参数名：
'''
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;

printme(str="My string");
###下例能将关键字参数顺序不重要展示得更清楚：
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

printinfo(age=50, name="miki");

##缺省参数
'''
调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
'''
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

printinfo(age=50, name="miki");
printinfo(name="miki");

##不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
'''
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
#加了星号（*）的变量名会存放所有未命名的变量参数。不定长参数实例如下：
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;

printinfo(10);
printinfo(70, 60, '50');

##匿名函数
'''
python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
###lambda函数的语法只包含一个语句，如下：
###lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)


##变量作用域
'''
一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
全局变量
局部变量
'''

##全局变量和局部变量
'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：
'''
total = 0;  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;


# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total



		 #不定长参数 ,分为两种一种一个*,一种是两个*
#用函数打印学员的信息
'''
def lianxi(name,age,sex='男',*args,**parents):
    print('学员的姓名是%s'%name)
    print('学员的年级是%d'%age)
    print('学员的性别是%s'%sex)
    #在函数体里面不需要加*
    print(args)
    print(parents)
#需要注意:函数里面如果有默认值参数,还有一个*不定长参数的时候,默认值最好加上参数名,否则按照位置实参一一对应
#一个* 的参数返回的是元组,两个*返回的是字典
lianxi('张三',21,'男',13877778888,'166','red',father='张三丰',mother='李冰冰')
'''