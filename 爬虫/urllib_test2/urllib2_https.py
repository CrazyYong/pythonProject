#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request as url_re
import urllib.parse as url_pa      #数据解析
import ssl

# 忽略SSL安全认证
context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"
#url = "https://www.baidu.com/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
request = url_re.Request(url, headers = headers)

# 添加到context参数里
response = url_re.urlopen(request, context = context)

print (response.read().decode('utf-8'))
