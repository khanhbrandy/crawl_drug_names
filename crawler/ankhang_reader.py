"""
Created on 2021-02-012
Creator: khanh.tn
"""


import json
import requests
from lxml import etree
from io import StringIO

parser = etree.HTMLParser()
f = open('ankhang.json') 
data = json.load(f) 

base_url="https://www.nhathuocankhang.com/aj/Category/Products"
result = {}
for ele in data:
    for k, v in ele.items():
        params = {"Key": None, "PageSize": 10000, "PageIndex": 0, "Category": int(v)}
        response = requests.post(base_url, data=params)
        html = response.content.decode("utf-8")
        tree = etree.parse(StringIO(html), parser=parser)
        drug_names = tree.xpath('//ul[@class="cate  "]/li/a/div/img/@alt')
        for idx in range(len(drug_names)):
            drug_names[idx] = drug_names[idx].strip()
        result[k] = drug_names
        print(k, " : ", drug_names)
with open("ankhang_drugs.json", 'w', encoding='utf8') as output:
    json.dump(result, output, indent=4, ensure_ascii=False)

    