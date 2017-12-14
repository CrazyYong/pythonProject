import urllib.request as url_re

'''
Get:请求的url会附带参数
Post:请求不会附带参数
对于Get请求：查询参数在QueryString里保存
对于Post请求：查询参数在Form表单里保存
'''
##指定url,http协议，通过url中的字符串拼接得到
url='http://www.baidu.com/s?wd=ai'
#构建request
request=url_re.Request(url)
#返回响应
response=url_re.urlopen(request)

print(response.read().decode('utf-8'))