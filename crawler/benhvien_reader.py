"""
Created on 2021-02-012
Creator: khanh.tn
"""


import json
import requests

f = open('benhvien.json') 
data = json.load(f) 

result = {}
for ele in data:
    for k in ele.keys():
        result[k] = []

for ele in data:
    for k, v in ele.items():
        result[k].extend(v)
for ele in result:
    for k, v in result.items():
        for i in range(len(v)):
            if v[i].find(" – Đặt Mua ") != -1:
                words = v[i].split(" – Đặt Mua ")
                v[i] = words[0]
            elif v[i].find(" – Đặt mua ") != -1:
                words = v[i].split(" – Đặt mua ")
                v[i] = words[0]
            elif v[i].find(" – Đăt Mua ") != -1:
                words = v[i].split(" – Đăt Mua ")
                v[i] = words[0]
            elif v[i].find(" – Đăt mua ") != -1:
                words = v[i].split(" – Đăt mua ")
                v[i] = words[0]   
            elif v[i].find(" – ĐT ") != -1:
                words = v[i].split(" – ĐT ")
                v[i] = words[0]  
            elif v[i].find(" – Đặt Ngay ") != -1:
                words = v[i].split(" – Đặt Ngay ")
                v[i] = words[0]  
            elif v[i].find(" – Mua thuốc ") != -1:
                words = v[i].split(" – Mua thuốc ")
                v[i] = words[0]    
            elif v[i].find(" – Liên Hệ ") != -1:
                words = v[i].split(" – Liên Hệ ")
                v[i] = words[0]
            elif v[i].find(" – Liên hệ ") != -1:
                words = v[i].split(" – Liên hệ ")
                v[i] = words[0]
            

# print(result)
with open("benhvien_drugs.json", 'w', encoding='utf8') as output:
    json.dump(result, output, indent=4, ensure_ascii=False)

    