'''
这是一个豆瓣读书作者的爬虫

'''

from urllib import request
import re


class Spider():
    url = 'https://music.douban.com'
    root_pattern = '<div class="author">([\s\S]*?)</div>'


    
#导入网站信息
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    

    def __analysis(self, htmls):
        html = re.findall(Spider.root_pattern, htmls)
        finish_data = [' '.join([i.strip() for i in price.strip().split('\t')]) for price in html]#去除空格，换行符和制表符
        print(finish_data)
        
        
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()