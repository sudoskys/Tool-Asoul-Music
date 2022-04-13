# From https://github.com/liuyunhaozz/bilibiliDownloader

import os
import time
import urllib
import requests


class fileGet(object):
    def __init__(self):
        self.debug = False

    def well(self, name):
        # import string
        name = name.replace('"', '_')  # 消除目标对路径的干扰
        name = name.replace("'", '_')  # 消除目标对路径的干扰
        # remove = string.punctuation
        table = str.maketrans(r'~!#$%^&,[]{}\/？?', '________________', "")
        return name.translate(table)

    def getAudio(self, item, dirname):
        baseUrl = 'http://api.bilibili.com/x/player/playurl?fnval=16&'
        if not os.path.exists(dirname):  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(dirname)
        st = time.time()
        bvid, cid, title = item[0], item[1], item[2]
        url = baseUrl + 'bvid=' + bvid + '&cid=' + cid
        # print(url)
        title = self.well(title)
        audioUrl = requests.get(url).json()['data']['dash']['audio'][0]['baseUrl']
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
        time.sleep(1)
        return os.path.join(dirname, title + '.mp3'))
