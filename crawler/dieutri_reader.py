"""
Created on 2021-02-012
Creator: khanh.tn
"""


import json
import requests

f = open('dieutri.json') 
data = json.load(f) 

result = []
for ele in data:
    for k in ele.keys():
        result.extend(ele[k])

print(len(result))
with open("dieutri_drugs.json", 'w', encoding='utf8') as output:
    json.dump(result, output, indent=4, ensure_ascii=False)

    