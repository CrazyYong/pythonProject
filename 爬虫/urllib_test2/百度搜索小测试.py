import urllib.request as url_re
import urllib.parse as url_pa      #数据解析


url='http://www.baidu.com/s'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.104 Safari/537.36'}

keyword=input('请输入要查询的关键字...')

wd={'wd':keyword}

wd=url_pa.urlencode(wd)

fullurl= url+"?"+wd

print(fullurl)

request=url_re.Request(fullurl,headers=headers)

response=url_re.urlopen(request)

print(response.read().decode('utf-8'))
