from bs4 import BeautifulSoup
import requests
from lxml import etree

#自定义字符串
html='''
<html>
<head><title>aibeifeng</title></head>
<body>
<p class="title" name="k"><b>aibeifeng</b></p>
<p class="title" name="k"><b>aibeifeng</b></p>
<p class="title" name="k"><b>aibeifeng</b></p>
<a href="http://www.baidu.com/k1" class="AI"><!--Boy--></a>
<a href="http://www.baidu.com/k2" class="AI02" id="02">io</a>
<a href="http://www.baidu.com/k3" class="AI" id="03">pool</a>
</body>
</html>
'''
#创建对象
soup=BeautifulSoup(html,'lxml')
#格式化输出
#print(soup.prettify())

#1.   tag    HTML中的标签
# print(soup.title)
# print(soup.head)
# print(soup.a)    #多个标签名相等的情况下，输出第一个满足条件的标签
#
# print(type(soup.a))

##1.1  tag的name属性
#print(soup.head.name)   ##返回当前标签的名称

#1.2   tag的attrs属性
# print(soup.a.attrs)   ##返回当前标签的类属性，以及所属的name，返回的是字典形式
#
# print(soup.a.get('class'))
#
# soup.a['class']='new'
# print(soup.a)

#2.   NavigableString   获取标签中的文本内容

# print(soup.p.string)  #文本内容
#
# print(type(soup.p.string))
#
# #BeautifulSoup   特殊tag,返回当前文档的全部内容
#
# print(type(soup.name))

##comment   获取注释内容(文本)，没有注释符号
print(soup.a.string)
print(type(soup.a.string))
## comment

#遍历文档树
#直接子节点：
#print(soup.head.contents)   ##返回当前节点的直接子节点，列表形式

#children 节点
#循环遍历当前节点的所有子节点
# for child in soup.body.children:
#     print(child)
#循环遍历当前节点的所有子孙节点（层次化输出）
# for child in soup.descendants:
#     print(child)

# print(soup.head.string)   ##当前标签只含有唯一标签时，返回最内层的文本
#
# print(soup.title.string)   #不嵌套，直接返回内容
#返回多个文本内容
# for string in soup.strings:
#     print(str(string))

#去空格化的文本内容返回
# for string in soup.stripped_strings:
#     print(str(string))

##搜索文档树：  tag

#find_all(name,attrs,text````)

#name参数

# print(soup.find_all('b'))
# print(soup.find_all('a'))

#正则表达式
import re
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

#列表
#print(soup.find_all(["a","b"]))

#布尔值,可以匹配任何节点
# for tag in soup.find_all(True):
#     print(tag)
# for tag in soup.find_all(False):
#     print(tag)

#keyword 参数
#print(soup.find_all(href="http://www.baidu.com/k2"))

#print(soup.find_all(href=re.compile("k2")))

#print(soup.select('.AI'))  #   .  代表class类，   #  代表id值

#print(soup.select("#02"))

#指定多个名称参数，过滤tag属性
#print(soup.find_all(href=re.compile("k"),id='02'))

#print(soup.find_all('a',class_='AI02'))

#text 参数
#print(soup.find_all(text=['io','pool']))

#limit  限制返回结果的个数，减少资源的消耗

print(soup.find_all('a',limit=2))

#//*[@id="content"]/ul[1]/li[1]/a



