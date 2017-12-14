from urllib import request

url='http://www.ibeifeng.com'
#代理IP
proxy={'http':'61.163.39.70:9999'}
#创建一个ProxyHandler
proxy_sp=request.ProxyHandler(proxy)
#创建一个opener
opener=request.build_opener(proxy_sp)
#user-agent
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
#安装opener
request.install_opener(opener)
#使用opener
response=request.urlopen(url)

opener.ope
#读取信息
print(response.read().decode('gbk'))