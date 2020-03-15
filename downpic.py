from bs4 import BeautifulSoup
import re
import requests
import os
from urllib import error

List = []
num = 0
numPicture = 0
file = ''

def Find(url):
    global List
    print('正在检测图片数量,请稍候.......')
    t = 0
    s = 0
    i = 1
    while t < 1000:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
               List.append(pic_url)
               t = t + 60
    return s

def dowmloadPicture(html, keyword):
    global num
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    print('找到关键字:' + keyword + '的图片，及将开始下载...')
    for each in pic_url:
        print('正在下载' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=10)
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = file + r'\\' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return

if __name__ == '__main__':
    word = input("请输入搜索关键词(可以说人名, 地名): ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    tot = Find(url)
    print('经过检验%s图片共有%d张'%(word, tot))
    numPicture = int(input('请输入想要下载图片的数量:'))
    file = input('请建立一个存储图片的文件夹，输入文件夹名称即可:')
    y = os.path.exists(file)
    if y == 1:
        print('该文件已经存在，请重新输入')
        file = input('请建立一个存储图片的文件夹，输入文件夹名称即可:')
        os.mkdir(file)
    else:
        os.mkdir(file)
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            print(url)
        except error.HTTPError as e:
            print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            dowmloadPicture(result.text, word)
            t = t + 60

    print('当前下载结束，感谢使用')