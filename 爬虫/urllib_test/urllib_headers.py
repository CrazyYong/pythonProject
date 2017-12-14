import urllib.request as url_re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.104 Safari/537.36'}

url='http://www.baidu.com/s?wd=ai'

request=url_re.Request(url,headers=headers)
# request.add_header(headers)#add_header()方法添加一个header
#返回响应
response=url_re.urlopen(request)

# print(response.read().decode('utf-8'))
# print(response.getcode())#返回响应吗
# print(response.geturl())#返回实际数据的实际url，防止重定向
# print(response.info())#返回服务器响应的http报头信息
print(request.get_header('User-agent'))