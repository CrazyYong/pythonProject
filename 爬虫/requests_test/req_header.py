import requests

user_agent='User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

headers={'User-Agent':user_agent}

r=requests.get('http://www.baidu.com',headers=headers)

#print(r.text)

print(r.content.decode('utf-8'))