#!/usr/bin/python3
#coding=utf-8

#字符串类



##Python访问字符串中的值
var1 = 'Hello World'
var2 = 'Python Ruonob'
print 'var1[0]:',var1[0]
print 'var2[1:5]:',var2[1:6]


##Python字符串更新
var1 = 'Hello World'
print '更新字符串：-',var1[:6]+'Runoob!'

##Python转义字符
print '我\000在' ###\000 表示 空格
print '我\'在'   ###\' 表示单引号
print '我\"在'   ###\" 表示双引号
print '我\n在'   ###\n 换行
print '我\r在'   ###\r 表示回车


##Python字符串运算符
a='Hello'
b='Pyton'
print a * 2   ###重复输出字符串
print a[1]    ###通过索引获取字符串中字符
print a[1:4]  ###截取字符串中的一部分
print "H" in a ###成员运算符 - 如果字符串中包含给定的字符返回 True
print "M" not in a  ###成员运算符 - 如果字符串中不包含给定的字符返回 True
print r'\n' ###原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
            ###原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。


##Python 字符串格式化
'''
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
'''
print "My name is %s and weight is %d kg!" % ('Zara', 21)

mm='我的名字是{name},我的年纪是{age}'
ss=mm.format(name='哈士奇',age=5)
print(ss)
ss=mm.format_map({'name':'哈士奇','age':5})
print(ss)


##Python三引号（triple quotes）
###python中三引号可以将复杂的字符串进行复制:
###python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
###三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）

hi = '''hi
there'''
print hi
###三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
###一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print errHTML


##Unicode 字符串
###Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单：
m = u'Hello World!'
print m
###引号前小写的"u"表示这里创建的是一个 Unicode 字符串。
###如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：
y = u'Hello\u0020World!'
print y


##python的字符串内建函数
###capitalize()方法,将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
s = 'a, B'
print s.capitalize()

###center()方法返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
str = 'runoob'
print str.center(20,'*')
print str.center(20)

##count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
str = "this is string example....wow!!!";
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

##decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。
str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')

##endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，
## 否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);

## isalnum() 方法检测字符串是否由字母和数字组成。
str = "this2009";  # 字符中没有空格
print str.isalnum();

str = "this is string example....wow!!!";
print str.isalnum();

## join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );