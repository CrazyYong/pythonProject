import urllib.request as url_re
import urllib.parse as url_pa      #数据解析

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
        "start":"0",
        "limit":"20"
    }

data = url_pa.urlencode(formdata).encode(encoding='UTF8')


request = url_re.Request(url, data = data, headers = headers)

print (url_re.urlopen(request).read().decode('utf-8'))



