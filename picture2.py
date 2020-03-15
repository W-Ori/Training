'''
这是一个爬取洛阳理工学院图片的爬虫
适用于大多数的 百度图片 中 链接 的下载
但是无法解决 HTTP Error

'''

from urllib import request
import re
import urllib
import uuid
import os

print('洛阳理工学院图片链接: https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1567305363296_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%B4%9B%E9%98%B3%E7%90%86%E5%B7%A5')
url1 = input("请输入你想下载图片的百度图片链接(请确保链接中没有中文字符)：")
print('抱歉目前下载图片个数随缘')

# 请求
Request = request.urlopen(url1)
print(request)
# 爬取链接获取html
Response =Request.read()
Response = Response.decode('utf-8')
print(Response)
# 正则表达式截取图片路径
urlList=re.findall(r'"objURL".{20,99}jpg',Response)
print('获取网址1',urlList)

i=0
for imgurl in urlList:
 
    i=int(i)
    #去除多余字符串
    imgurl=imgurl.lstrip('"objURL":')
    print('获取链接',imgurl)

    Request=urllib.request.urlopen(imgurl)
    Response = Request.read()
    print(Response)
    i+=1
 
    filename=str(uuid.uuid1())+'.jpg'
    fileurl="d:/爬取图片的文件夹/"
    print('保存路径', fileurl)
 
    #判断路径是否存在,不存在则创建路径
    if os.path.isdir(fileurl):
        print()
    else:
        os.mkdir(fileurl)
 
    file = open(fileurl+filename, 'wb')
    #打印结果
    file.write(Response)
    print('次数', i)
 
    file.close()