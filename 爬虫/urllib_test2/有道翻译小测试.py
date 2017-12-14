import urllib.request as url_re
import urllib.parse as url_pa      #数据解析
# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 完整的headers
headers = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With" : "XMLHttpRequest",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    }

# 用户接口输入
key = input("请输入需要翻译的文字:")

# 发送到web服务器的表单数据
formdata = {
"type" : "AUTO",
"i" : key,
"doctype" : "json",
"xmlVersion" : "1.8",
"keyfrom" : "fanyi.web",
"ue" : "UTF-8",
"action" : "FY_BY_CLICKBUTTON",
"typoResult" : "true"
}

# 经过urlencode转码
data = url_pa.urlencode(formdata).encode(encoding='UTF8')

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = url_re.Request(url, data = data, headers = headers)

print (url_re.urlopen(request).read().decode('utf-8'))

