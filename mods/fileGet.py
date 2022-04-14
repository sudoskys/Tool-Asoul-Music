# encoding: utf-8
# From https://github.com/liuyunhaozz/bilibiliDownloader

import os
import time
import urllib
import requests
import random

class fileGet(object):
    def __init__(self):
        self.debug = False
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate ,br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Referer': 'https://api.bilibili.com/',
            'Connection': 'keep-alive',
            'Host': 'api.bilibili.com',
            #'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Cookie': '1P_JAR=2022-02-09-02;SEARCH_SAMESITE=CgQIv5QB;ID=CgQIsv5QB0',

            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'cross-site',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
        }
    
    def random_sleep(self, mu=3, sigma=1.7):
            """正态分布随机睡眠
            :param mu: 平均值
            :param sigma: 标准差，决定波动范围
            """
            secs = random.normalvariate(mu, sigma)
            if secs <= 0:
                secs = mu  # 太小则重置为平均值
            time.sleep(secs)

        
    def well(self, name):
        # import string
        name = name.replace('"', '_')  # 消除目标对路径的干扰
        name = name.replace("'", '_')
        # remove = string.punctuation
        table = str.maketrans(r'~!#$%^&,[]{}\/？?', '________________', "")
        return name.translate(table)

    def getAudio(self, item, dirname):
        baseUrl = 'https://api.bilibili.com/x/player/playurl?fnval=16&'
        if not os.path.exists(dirname):  # 创建为文件夹
            os.makedirs(dirname)
        st = time.time()
        bvid, cid, title = item[0], item[1], item[2]
        apiUrl = baseUrl + 'bvid=' + bvid + '&cid=' + cid
        print(title+ '---'+str(bvid) + '---->'+apiUrl)
        title = self.well(title)
        audioSong = requests.get(url=apiUrl, headers=self.header).json()
        if not audioSong.get("code")==0:
            raise Exception("BiliBili Api 访问异常!... \n Detail:" + str(audioSong)+' \n 目标Url:'+ str(apiUrl))
        audioUrl=audioSong.get('data').get('dash')['audio'][0]['baseUrl']
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
            ('Accept', '*/*'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Accept-Encoding', 'gzip, deflate, br'),
            ('Range', 'bytes=0-'),
            ('Referer', 'https://api.bilibili.com/x/web-interface/view?bvid=' + bvid),  # referer 验证
            ('Origin', 'https://www.bilibili.com'),
            ('Connection', 'keep-alive'),
        ]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url=audioUrl, filename=os.path.join(dirname, title + '.mp3'))
        ed = time.time()
        # 回调函数
        # print(str(round(ed-st,2))+' seconds download finish:',title)
        self.random_sleep()
        return os.path.join(dirname, title + '.mp3')
