import re
import requests
import time
from urllib.parse import urlencode
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
param_dict = {
    'year': 2018,  # 年
    'issue': '01',  # 月
    'pykm': 'XDCB',  # 期刊
    'pageIdx': 0,
    'pcode': 'CJFD'
}

now_year = 2018
max_year = 2020
now_month = 1

while now_year <= max_year:
    for i in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
        print('发表时间在', now_year, '年', now_month, '月的：')
        param_dict["year"] = now_year
        param_dict["issue"] = i
        response = requests.get(url + urlencode(param_dict), headers=headers)
        if now_month < 12:
            now_month += 1
        else:
            now_month = 1
            now_year += 1
        bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for i in bs.select('dd'):  # 路径
            title = i.select_one('span.name>a').text  # 标题
            title = re.sub("\s", "", title)  # 去除空格
            author = i.select_one('span.author').text  # 作者
            print('标题：', title)
            print('作者：', author)
        time.sleep(3)
