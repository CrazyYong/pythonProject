import urllib.request as url_re

##指定url,http协议，通过url中的字符串拼接得到
url='http://www.baidu.com/s?wd=ai'
#构建request
request=url_re.Request(url)
#返回响应
response=url_re.urlopen(request)

print(response.read().decode('utf-8'))