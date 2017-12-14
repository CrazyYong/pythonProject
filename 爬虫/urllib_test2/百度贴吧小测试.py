import urllib.request as url_re
import urllib.parse as url_pa      #数据解析


def loadPage(url,filname):
    '''
    作用：根据url发送请求，获取服务器响应文件
    url:需要爬取的url地址
    '''
    print('正在下载'+filname)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.104 Safari/537.36'}

    request=url_re.Request(url,headers=headers)
    return url_re.urlopen(request).read().decode('utf-8')

def writePage(html,filename):
    '''
    作用：将Html内容写入到本地
    :param html: 服务器相应文件内容
    '''
    print('正在保存'+filename)
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

    print('-'*30)

'''
作用：贴吧爬虫调度器，负责组合处理每个页面url
        url:贴吧url的前部分
        beginPage:起始页
        endPage:结束页
'''
def tiebaSpider(url,beginPage,endPage):

    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        filename='第'+str(page)+'页.html'
        fullurl=url+'&pn='+str(pn)
        # print(fullurl)
        html=loadPage(fullurl,filename)
        # print(html)
        writePage(html,filename)



kw=input('请输入需要爬取的贴吧名字')
beginPage=int(input('请输入起始页:'))
endPage=int(input('请输入结束页:'))

url='http://tieba.baidu.com/f?'
key=url_pa.urlencode({'kw':kw})
fullurl=url+key
tiebaSpider(fullurl,beginPage,endPage)