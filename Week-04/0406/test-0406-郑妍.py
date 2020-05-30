import time
import re
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
import datetime
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
param_dict = {
    'year': 2018,
    'issue': '01',
    'pykm': 'XDCB',
    'pageIdx': 0,
    'pcode': 'CJFD'
}
now_month = 1
now_year = 2018
max_year = 2020
while now_year < datetime.datetime.now().year or now_year == datetime.datetime.now().year and now_month <= datetime.datetime.now().month:
    print('正在请求',now_year,'年',now_month,'月')
    param_dict["year"] = now_year
    if now_month < 10:
        param_dict["issue"] = '0' + str(now_month)
    else:
        param_dict["issue"] = now_month
    response = requests.get("http://new.gb.oversea.cnki.net/knavi/JournalDetail/GetArticleList?" + urlencode(param_dict), headers=headers)
    bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
    for i in bs.select('dd'):
        name = i.select_one('span.name').text
        title = re.sub("^\s*|\s*$", "", name)
        author = i.select_one('span.author').text
        if author == '':
            pass
        else:
            print('标题：',title,'作者：',author)
    if now_month < 12:
        now_month += 1
    else:
        now_month = 1
        now_year +=1
    time.sleep(1)
