import urllib.request

try:
    response=urllib.request.urlopen('http://www.ibeifeng.com')
    print(response)
except urllib.request.HTTPError as e:
    #hasattr()  判断对象（上述IP）是否存在
    if hasattr(e,'code'):
        print('Erroe code:',e.code)    ##e.code   返回HTTP状态码