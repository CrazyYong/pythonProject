import requests
r=requests.get('http://www.baidu.com')

r.encoding='utf-8'

print(type(r))    #结果类型

print(r.status_code)   #状态码

print(r.encoding)  #编码方式

print(r.cookies)  #cookies内容

print(r.content)  #html内容，以字节形式

print(r.text)  #html内容，以文本形式