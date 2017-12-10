import urllib.request
import http.cookiejar

#定义文件
filename='cookie.txt'

#申明cookie对象
cookie=http.cookiejar.MozillaCookieJar(filename)

#构建cookie处理
handler=urllib.request.HTTPCookieProcessor(cookie)

#构建一个opener
opener=urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

#open方法，传入url
response=opener.open('http://www.ibeifeng.com')

#保存文件
#ignore_discard,如果cookie被丢弃，是否保存
#ignore_expires,如果在该文件中cookie已经存在，是否覆盖
cookie.save(ignore_discard=True,ignore_expires=True)