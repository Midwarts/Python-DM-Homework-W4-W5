'''
爬取知网“现代传播”
'''

from urllib.parse import urlencode
import requests
import time
from bs4 import  BeautifulSoup
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
param_dict = {
'year': 2018,      #年份
'issue':'01',       #月份
'pykm': 'XDCB',    #期刊名
'pageIdx': 0,
'pcode': 'CJFD'
}

now_year=2018
max_year=2020
now_month=1                 #这里期数是01格式的 不能加很麻烦
max_month=12

while now_year<=max_year:
    for i in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:         #因为不能加只能列表套现
        print(now_year, '年', now_month, '月')
        param_dict["year"]=now_year       #修改参数
        param_dict["issue"]=i
        response=requests.get('http://navi.cnki.net/knavi/JournalDetail/GetArticleList?'+  urlencode(param_dict),headers=headers)  #获取参数
        bs=BeautifulSoup(response.content.decode(errors="ignore"),'lxml')   #获取一锅汤
        for i in bs.select('dd'):       #包含作者和标题的路径
          title=i.select_one('span.name>a').text      #提取标题
          title=re.sub("\s", "",title)     #去除空格
          author=i.select_one('span.author').text    #提取作者
          print('标题：',title)
          print('作者：',author)
        time.sleep(2)
        if now_month<12:          #获取不同年份、月份
            now_month+=1
        else:
            now_month=1
            now_year+=1