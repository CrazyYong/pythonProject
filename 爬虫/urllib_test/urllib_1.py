import urllib.request
#穿入一个协议，HTTP协议
#urllib.request.urlopen(url,data,timeout)
#url   目标网址，URL
#data  访问url时发送的数据包
#timeout   设置超时时间

#返回response对象

response=urllib.request.urlopen("http://www.ibeifeng.com")

#通过read方法，读取网页的源代码，返回字节对象

print(response)