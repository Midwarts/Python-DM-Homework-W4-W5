if __name__ == '__main__':
    from urllib.parse import urlencode
    from bs4 import BeautifulSoup
    import time
    import requests

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    }  # Headers
    param_dict = {
        'year': 2020,
        'issue': '04',
        'pykm': 'XDCB',
        'pageIdx': 0,
        'pcode': 'CJFD',
    }  # 参数列表
    now_year=2018
    max_year=2020
    while now_year <= max_year:
        now_month=1
        print("正在请求第", now_year, "年......")
        param_dict["year"] = now_year  # 将当前页填入到参数列表中
        while now_month<13:
            if now_month<10:
                k=str(now_month)
                now_month=k.zfill(2)
            else:
                now_month=now_month
            print("正在请求第", now_month, "月......")
            param_dict['issue']=now_month
            url="https://navi.cnki.net/knavi/JournalDetail/GetArticleList?"
            response=requests.get(url+urlencode(param_dict))
            paper=BeautifulSoup(response.content.decode(errors="ignore"),'lxml')
            for words in paper.select('dd'):
                name=words.select_one("span.name")
                print('标题',name)
                author=words.select_one("span.author")
                print('作者：',author)
            now_month=int(now_month)
            now_month+=1
        now_year+=1
        time.sleep(3)

