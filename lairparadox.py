# -*- coding:utf-8 -*-

import requests
import os
import sys
from bs4 import BeautifulSoup

os.chdir(sys.path[0])

if __name__ == "__main__":
        url = 'https://plato.stanford.edu/entries/liar-paradox' #1.指定url
        response = requests.get(url=url) #2. 发起请求
        page_text = response.text #3.获取响应数据(字符串形式
        #print(page_text)
        with open('./liarparadox.html','w',encoding='utf-8') as fp:
                fp.write(page_text)
        print("爬取完毕") #4.持久化存储

        fp = open('./liarparadox.html','r',encoding='utf-8') #5.数据解析
        soup = BeautifulSoup(fp,'lxml')
        list = soup.find_all('p') #找到符合要求的所有标签(作为列表)
        for i in list: #将列表中的元素逐个打印为text(即去掉<p>标签)并存储为本地txt
                print(i.text,file=open('./liarparadox.txt','a',encoding='utf-8')) 
        print("存储完毕")



