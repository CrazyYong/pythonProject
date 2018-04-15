#!/usr/bin/python3
#coding=utf-8
import time;  # 引入time模块
import calendar
import datetime


#日期和时间
'''
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
'''
ticks = time.time()
print ("当前时间戳为:", ticks)

##获取当前时间
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)


##获取格式化的时间
localtime = time.asctime(time.localtime(time.time()) )
print ("本地时间为 :", localtime)

##格式化日期
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

##python中时间日期格式化符号：
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

##获取某月日历
cal = calendar.month(2017, 12)
print ("以下输出2016年1月份的日历:")
print (cal);

##Time 模块
print (time.timezone)
print (time.tzname)

##日历（Calendar）模块
print (calendar.isleap(2017))  #是闰年返回True，否则为false。
print (calendar.firstweekday()) #返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
print (calendar.leapdays(2005,2017))#返回在Y1，Y2两年之间的闰年总数。


##datetime包
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)



