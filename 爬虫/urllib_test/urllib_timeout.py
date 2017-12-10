from urllib import request
#可以自定义访问时间，超出值则断开连接，返回timeout

response=request.urlopen('http://www.ibeifeng.com',timeout=0.1)
print(response.read().decode('gbk'))