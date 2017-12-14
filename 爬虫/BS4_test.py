from bs4 import BeautifulSoup
from lxml import etree
import requests
import codecs
import re

url='http://www.runoob.com/python/python-100-examples.html'

def getUrl(baseurl):
    x=requests.get(baseurl)
    x.encoding='utf-8'
    soup=BeautifulSoup(x.text,'lxml')
    for i in soup.find_all('a',href=re.compile('^/python/python-exercise')):
        url=i.get('href')
        yield (url)

def getCont(burl):
    for rurl in burl:
        wholeurl='http://www.runoob.com'+rurl
        x=requests.get(wholeurl)
        x.encoding='utf-8'
        soup=BeautifulSoup(x.text,'lxml')
        title=soup.find('div',class_="article-intro")
        titletext=title.h1.string
        cont=title.find_all('p')
        list1=[]
        i=1
        while True:
            if re.match('程序源代码：',str(cont[i].text)) or re.match(' Python 100例',str(cont[i].text)) or re.match('以上实例输出结果为：',str(cont[i].text)):
                break
            else:
                list1.append(cont[i].text)
                i+=1
                print(list1)
        yield (titletext,list1)

purl=getUrl(url)
text=getCont(purl)

f=open('k.txt','wb')
w=lambda x:f.write((x+'\n').encode('utf-8'))
for num,list2 in text:
    f.write(b'*'*100+b'\n')
    w(num)
    for j in range(len(list2)):
        w(list2[j])
f.close()

