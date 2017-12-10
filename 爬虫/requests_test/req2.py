import requests

postdata={'qlx':'value1','kkk':'value2'}

r=requests.post('http://httpbin.org/get',data=postdata)

print(r.text)
print(r.status_code)