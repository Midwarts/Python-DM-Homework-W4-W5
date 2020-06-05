import re
import requests
import time
from bs4 import BeautifulSoup
import json

from lxml.builder import unicode

def clear_polar_space(text):
    """
    清除前后空格(清除字符串前后两端的空白字符)
    """
    text = re.sub("^[ \xa0]*", "", text)
    text = re.sub("[ \xa0]*$", "", text)
    return text

#修改headers请求进入，否则无法看见文章标题作者等信息
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'Ecp_ClientId=2200424150102886087; cnkiUserKey=9e8a35e1-9a1a-5329-b21a-f6bcc880d2be; ASP.NET_SessionId=3x5cppkgzks0qp5mtfo5o3bm; SID_navi=1201620; Ecp_IpLoginFail=200603218.20.10.118',
        'Host': 'navi.cnki.net',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

}
paper_list = []

#获取2017-2019年的论文
for year in range(2017,2019):
    a = "https://navi.cnki.net/knavi/JournalDetail/GetArticleList?year={0}".format(year + 1)#因为同时有年份和月份，所以就想着把URL拆开两部分循环.
    for month in range(12):#月份为一位数的时候有0，所以分成两部分循环
        if month < 9:
            url = ""
            b ="&issue=0{0}&pykm=XDCB&pageIdx=0&pcode=CJFD".format(month+1)
            url = a+b
            #print(url)
        else:
            url=""
            b ="&issue={0}&pykm=XDCB&pageIdx=0&pcode=CJFD".format(month+1)
            url = a+b
            #print(url)
        response = requests.get(url, headers=headers)
        bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        time.sleep(5)

#bs = BeautifulSoup(response.content.decode(errors="ignore"), 'lxml')
        for keyword_label in bs.select("body"):#NetWork里面open in new tab发现标签变为body
            for i in keyword_label:#body是一整块页面，i属于它里面的每项，栏目与文章并列
                if len(i)  == 1:#print(type)发现由NavigableString格式的数据，不可以用select。因为len=1和文章类型一样，实在不知道怎么去掉，就转成了类string用正则匹配。
                    i= unicode(i.string)
                    paper_type = re.findall(r'([\u4E00-\u9FA5]+)',i)
                    if len(paper_type)>0:
                        paper_list.append({"type":paper_type})

                else:
                    #print(len(i))
                    print("循环")
                    #提取、清洗标题
                    if len(i)>0:
                        paper_name=i.select_one("body > dd > span.name > a").text
                        paper_name=clear_polar_space(paper_name)

                        print(paper_name)



                    #提取作者
                        paper_author=i.select_one("body > dd > span.author").text
                    #提取、清洗链接
                        paper_url=i.select_one("body > dd > ul > li.J_btnShare.btn-share > ul > li > a")["onclick"]
                        paper_url=re.findall(r'//kns.cnki.net\S+\d',paper_url)

                        print("next")



                        paper_list.append({
                         "title": paper_name,
                         "author": paper_author,
                          "link":paper_url
                        })
time.sleep(3)
print(paper_list)
#print(type_list)



# 将临时变量中的数据存储到Json文件
with open("知网传播观察.json", "w+", encoding="UTF-8") as file:
    file.write(json.dumps({"data": paper_list}, ensure_ascii=False))


print('done')
