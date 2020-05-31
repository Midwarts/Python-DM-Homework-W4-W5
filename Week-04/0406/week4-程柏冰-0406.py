import time
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}  # Headers

param_dict = {
    "year": 2018,
    "issue": "01",
    "pykm": 'XDCB',
    "pageIdx": 0,
    "pcode": 'CJFD'
}  # 参数列表

now_year = 2018
max_year = 2020

if __name__ == "__main__":
    while now_year <= max_year:
        now_issue = 1
        while now_issue < 13:
            if now_issue < 10:
                k = str(now_issue)
                now_issue = k.zfill(2)
            else:
                now_issue = now_issue
            print("正在请求第", now_year, "年","第", now_issue, "期......")
            param_dict["year"] = now_year
            param_dict['issue'] = now_issue
            url = "https://navi.cnki.net/knavi/JournalDetail/GetArticleList?"
            response = requests.get(url + urlencode(param_dict))
            bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
            for item in bs.select('dd'):
                name = item.select_one("span.name")
                print('标题', name)
                author = item.select_one("span.author")
                print('作者：', author)
            now_issue = int(now_issue)
            now_issue += 1
        now_year += 1
        time.sleep(3)

#问题：有时候可以抓出来，有时候就只有期刊序号
