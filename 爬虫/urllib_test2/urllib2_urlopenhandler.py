#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request

# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
#http_handler = urllib2.HTTPHandler()

# 在HTTPHandler增加参数"debuglevel=1"将会自动打开Debug log 模式，
# 程序在执行的时候会打印收发包的信息
http_handler = request.HTTPHandler(debuglevel=1)

# 调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = request.build_opener(http_handler)

request = request.Request("http://www.baidu.com/")

response = opener.open(request)

print(response.read().decode('utf-8'))

#print response.read()

