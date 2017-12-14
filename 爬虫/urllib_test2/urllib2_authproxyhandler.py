#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request

authproxy_handler = request.ProxyHandler({"http" : "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
#authproxy_handler = urllib2.ProxyHandler({"http" : "114.215.104.49:16816"})

opener = request.build_opener(authproxy_handler)

request = request.Request("http://www.baidu.com/")

response = opener.open(request)

print (response.read())

