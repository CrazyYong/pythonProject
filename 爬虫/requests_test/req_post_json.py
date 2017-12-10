import json
import requests

url='http://httpbin.org/post'

playload={'some':'data'}

r=requests.post(url,data=json.dumps(playload))

print(r.text)