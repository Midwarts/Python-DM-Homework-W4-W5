from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
import re
import time
import math

# 章节目录与文章目录并列，我好像还是不大会处理这样的层次关系，所以只读取了文章目录quq
# 只尝试运行了“读取单期刊物”，运行无误
# 加上翻页后因内容过多且pycharm里的console好像有问题，担心被封，故没有进行调试（应该没有问题）


# 模拟头部访问
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Cookie": "Ecp_ClientId=4200525224904150157; cnkiUserKey=48c436da-ae12-a62c-1bbb-1b9a9d43e054; Ecp_IpLoginFail=20052936.35.6.250; ASP.NET_SessionId=utalzocisijlm14qzpj5ojng; SID_navi=120162; _pk_ses=*",
    "Host": "navi.cnki.net",
    "Origin": "https://navi.cnki.net",
    "Referer": "https://navi.cnki.net/knavi/JournalDetail?pcode=CJFD&pykm=XDCB",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

# 请求2020年的期刊
z = 1
for q in range(4):

    print("==================================2020年%d月刊==================================" %z)
    print()
    # 访问该期刊物
    response = requests.get("https://navi.cnki.net/knavi/JournalDetail/GetArticleList?year=2020&pykm=XDCB&pageIdx=0&pcode=CJFD&issue=0%d"%z ,headers=headers)

    # 读取文章目录
    bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
    i = 1

    for content in bs.select("body > dd"):
        article_page = content.select_one("dd > span.company").text
        article_author = content.select_one("dd > span.author").text
        link = content.select_one("dd > span.name > a")
        link = link.get("href")
        file_name = link.split("&")[2]
        article_url = "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTO&" + file_name
        article_name = content.select_one("dd > span.name > a").text
        article_name = article_name.strip()

        print("第", str(i), "篇   ", article_page, "页")
        print("篇名 ： 《%s》" % article_name)
        print("作者 ： ", article_author)
        print("链接 ： ", article_url)
        print()

        i += 1

    print("==================================本期内容读取完毕==================================" % z)
    print()
    print()
    z += 1
    time.sleep(3)

# 请求2019年的期刊
z = 1
for q in range(12):

    print("==================================2019年%d月刊==================================" %z)
    print()
    # 访问该期刊物
    response = requests.get("https://navi.cnki.net/knavi/JournalDetail/GetArticleList?year=2019&pykm=XDCB&pageIdx=0&pcode=CJFD&issue=0%d"%z ,headers=headers)

    # 读取文章目录
    bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
    i = 1

    for content in bs.select("body > dd"):
        article_page = content.select_one("dd > span.company").text
        article_author = content.select_one("dd > span.author").text
        link = content.select_one("dd > span.name > a")
        link = link.get("href")
        file_name = link.split("&")[2]
        article_url = "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTO&" + file_name
        article_name = content.select_one("dd > span.name > a").text
        article_name = article_name.strip()

        print("第", str(i), "篇   ", article_page, "页")
        print("篇名 ： 《%s》" % article_name)
        print("作者 ： ", article_author)
        print("链接 ： ", article_url)
        print()

        i += 1

    print("==================================本期内容读取完毕==================================" % z)
    print()
    print()
    z += 1
    time.sleep(3)

# 请求2018年的期刊
z = 1
for q in range(12):

    print("==================================2018年%d月刊==================================" %z)
    print()
    # 访问该期刊物
    response = requests.get("https://navi.cnki.net/knavi/JournalDetail/GetArticleList?year=2018&pykm=XDCB&pageIdx=0&pcode=CJFD&issue=0%d"%z ,headers=headers)

    # 读取文章目录
    bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
    i = 1

    for content in bs.select("body > dd"):
        article_page = content.select_one("dd > span.company").text
        article_author = content.select_one("dd > span.author").text
        link = content.select_one("dd > span.name > a")
        link = link.get("href")
        file_name = link.split("&")[2]
        article_url = "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTO&" + file_name
        article_name = content.select_one("dd > span.name > a").text
        article_name = article_name.strip()

        print("第", str(i), "篇   ", article_page, "页")
        print("篇名 ： 《%s》" % article_name)
        print("作者 ： ", article_author)
        print("链接 ： ", article_url)
        print()

        i += 1

    print("==================================本期内容读取完毕==================================" % z)
    print()
    print()
    z += 1
    time.sleep(3)

print("全部内容读取完成√")