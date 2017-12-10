import urllib.request
import http.cookiejar

#申明cookie对象
cookie=http.cookiejar.MozillaCookieJar()

#从cookie文件中读取内容到变量
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)

request=urllib.request.Request('http://www.ibeifeng.com')

opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

response=opener.open(request)

print(response.read().decode('gbk'))