import re

'''
search 方法用于查找字符串的任何位置，它也是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果，它的一般使用形式如下：

search(string[, pos[, endpos]])

其中，string 是待匹配的字符串，pos 和 endpos 是可选参数，指定字符串的起始和终点位置，默认值分别是 0 和 len (字符串长度)。

当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
'''

pattern = re.compile('\d+')
m = pattern.search('one12twothree34four')  # 这里如果使用 match 方法则不匹配
m.group()
'12'
m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
m
m.group()
'34'
m.span()
(13, 15)