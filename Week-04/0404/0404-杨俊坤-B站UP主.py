'''
B站UP主发布视频信息采集
'''
from urllib.parse import urlencode
import requests
import time
import json

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://space.bilibili.com",
    "referer": "https://space.bilibili.com/10462362/video",
    "pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Upgrade-Insecure-Requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}  # Headers
'''
控制台扒取的数据：
mid：UP主的ID，可以通过UP主主页的Url获得
ps：当前页获取的视频数量
tid：视频标签类型
pn：当前页面数（从1开始计数）
keyword：搜索关键词（默认为空）
order：视频顺序（最新发布=pubdate、最多播放=click、最多收藏=stow）
jsonp：未知作用，可当常量使用
'''
param_dict = {
'mid': 10462362,
'ps': 30,
'tid': 0,
'pn': 1,
'keyword':"",
'order': "click",
'jsonp': "jsonp"
}
now_page = 1
max_page = 3
while now_page <= max_page:           #要在循环里读取数据
    print("第", now_page, "页:")
    param_dict["pn"] = now_page
    response = requests.get('https://api.bilibili.com/x/space/arc/search?mid=10462362&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'+urlencode(param_dict),headers=headers)
    json = response.json()  # 将返回结果解析为Json格式
    for i in json["data"]["list"]["vlist"]:  #括号里是大键
        title=i['title']
        length=i['length']
        play=i['play']
        print('标题：',title)
        print('时长：',length)
        print('播放量：',play)    #这样的大概思路是爬一页打印一页的数据 而不是存在列表里

    now_page += 1  # 循环 加一页

    time.sleep(3)