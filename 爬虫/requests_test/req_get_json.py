import requests

r=requests.get('https://github.com/timeline.json',stream=True)

print(r.text)

print(r.json())  ##json解析

print(r.raw)