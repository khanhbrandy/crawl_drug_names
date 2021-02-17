"""
Created on 2021-02-012
Creator: khanh.tn
"""

import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import json

class NhathuocBenhVien(scrapy.Spider):
    name = "longchau"
    def __init__(self):
        self.urls = [
                'https://www.dieutri.vn/',
        ]
        
        self.result = []
    def cleanStr(self, inputString):
        inputString = str(inputString)
        s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
        s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
        s = ''
        for c in inputString:
            if c in s1:
                s += s0[s1.index(c)]
            else:
                s += c
        s = s.replace('–', '')
        s = s.replace('-', '')
        s = s.replace('  ', ' ')
        s = s.replace(' ', '-')
        s = s.strip()
        return s.lower()

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_mainpage, cb_kwargs=dict(url=url))

    def parse_mainpage(self, response, url):
        # categories = {}
        names = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for name in names:
            link = url + '?q={}'.format(name.upper())
            for i in range(1, 10):
                link_next = link + '&page={}'.format(i)
                yield scrapy.Request(url=link_next, callback=self.parse_subpage)

    def parse_subpage(self, response):
        item = CrawlerItem()
        item['Name'] = response.xpath('//div[@class="result-item"]/a/text()').extract()
        if item['Name']:
            yield item
        else:
            pass
        

        
        
                






    