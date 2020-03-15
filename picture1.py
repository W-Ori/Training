
import re
import time
import os
from urllib import request
import requests

#获取目标网址HTML
def getHtml(url):
    page = request.urlopen(url)
    htmld = page.read()
    html = htmld.decode('utf-8')
    return html

def getImg(html):
    urlList = re.findall(r'"objURL".{20,99}jpg', html)
    
    return urlList

def save_file(urlList):
    for urls in urlList:
        urls = urls.lstrip('objURL":')
        root = 'D://pics//'
        path = root + urls.spilt('/')[-1]

        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(urls)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('爬取成功')
        else:
            print('文件存在')
            
        


        





def go():
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%B4%9B%E9%98%B3%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2'
    html = getHtml(url)
    urlList = getImg(html)
    save_file(urlList)

go()
    


