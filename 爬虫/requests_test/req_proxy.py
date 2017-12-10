import requests

proxies={'http':'http://116.62.170.104:3128'}

r=requests.post('http://httpbin.org/post',proxies=proxies)

print(r.content.decode('utf-8'))