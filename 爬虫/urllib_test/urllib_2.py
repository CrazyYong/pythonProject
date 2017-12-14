import urllib.request

#构建一个request请求
request=urllib.request.Request("http://www.baidu.com")

#获取请求的响应
response=urllib.request.urlopen(request)

#以字节形式读取内容（必要时转码）
print(response.read().decode('gbk'))
