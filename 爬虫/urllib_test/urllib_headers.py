import urllib.request as url_re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.104 Safari/537.36'}

url='http://www.baidu.com/s?wd=ai'

request=url_re.Request(url,headers=headers)
#返回响应
response=url_re.urlopen(request)

print(response.read().decode('utf-8'))