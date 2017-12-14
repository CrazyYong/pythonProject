#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request

# 代理开关，表示是否启用代理
proxyswitch = False

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
httpproxy_handler = request.ProxyHandler({"http" : "124.88.67.54:80"})

# 构建了一个没有代理的处理器对象
nullproxy_handler = request.ProxyHandler({})

if proxyswitch:
    opener = request.build_opener(httpproxy_handler)
else:
    opener = request.build_opener(nullproxy_handler)



# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
request.install_opener(opener)

response = request.urlopen("http://www.baidu.com/")

print (response.read().decode("utf-8"))
