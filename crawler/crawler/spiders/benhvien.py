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
    name = "benhvien"
    def __init__(self):
        self.urls = [
                'https://nhathuocbenhvien.vn/',
        ]
        self.parents = ["menu-item-124", "menu-item-22"]
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
        names = []
        links = []
        for p in self.parents:
            names.extend(response.xpath('//li[@id="{}"]/ul/li//a/text()'.format(p)).extract())
        for name in names:
            link = url + self.cleanStr(name)
            links.append(link)

        for name, link in zip(names, links):
            for i in range(1,21):
                if i ==  1:
                    yield scrapy.Request(url=link, callback=self.parse_subpage, cb_kwargs=dict(name=name))
                else:
                    link_next =link + "/page/{}/".format(i)
                    yield scrapy.Request(url=link_next, callback=self.parse_subpage, cb_kwargs=dict(name=name))

    def parse_subpage(self, response, name):
        drug_names = response.xpath('//div[@class="product-item col-sm-3 col-md-15  col-xs-6"]/p/a/@title').extract()
        yield {name: drug_names}

        
        
                






    