import urllib.request as url_re
import urllib.parse as url_pa      #数据解析
#指定url,HTTP协议
url='http://www.zhihu.com/'

#建立数据包（字典形式）
post_data={'username':'admin','password':'123456'}
data=url_pa.urlencode(post_data)  #urlencode()方法使urllib解析为能懂的形式

request=url_re.Request(url)

#data数据，必须是字节型的字符串
response=url_re.urlopen(request,data.encode('utf-8'))

print(response.read().decode('utf-8'))


# wd={'wd':'你好啊'}
# new_wd=url_pa.urlencode(wd)
# # print(url_pa.unquote(new_wd))
# print(new_wd)