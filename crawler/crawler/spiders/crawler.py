"""
Created on 2021-02-012
Creator: khanh.tn
"""

import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import json

class NhathuocAnKhang(scrapy.Spider):
    name = "crawler"
    def __init__(self):
        self.urls = {
                'https://www.nhathuocankhang.com':'https://www.nhathuocankhang.com/thuoc',
        }
        self.result = []

    def start_requests(self):
        for main_url, url in self.urls.items():
            yield scrapy.Request(url=url, callback=self.parse_mainpage, cb_kwargs=dict(main_url=main_url))

    def parse_mainpage(self, response, main_url):
        # categories = {}
        names = response.xpath('//*[@class="nonecate"]/a/h3/text()').extract()
        links = response.xpath('//*[@class="nonecate"]/a/@data-id').extract()
        for name, link in zip(names, links):
            # categories[name] = main_url+link
            yield {name: link}
    # def parse_subpage(self, response, name):
    #     drug_names = response.xpath('//ul[@class="cate  "]/li/a/h3/text()').extract()
        
    #     for idx in range(len(drug_names)):
    #         drug_names[idx] = drug_names[idx].strip()
    #     yield {name: drug_names}
        
                




    # scrapy shell -s USER_AGENT='custom user agent' 'https://www.nhathuocankhang.com/thuoc'


    