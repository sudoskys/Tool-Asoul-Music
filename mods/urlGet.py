# encoding: utf-8
# From https://github.com/liuyunhaozz/bilibiliDownloader

import requests


class infoGet(object):
    def __init__(self):
        self.debug = False
        self.header= {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Referer': 'https://api.bilibili.com/',
            'Connection': 'keep-alive',
            'Host': 'api.bilibili.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Cookie': '1P_JAR=2022-02-09-02;SEARCH_SAMESITE=CgQIv5QB;ID=CgQIsv5QB0',
        }

    def getCidAndTitle(self, bvid, p=1):
        url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
        ciddata = requests.get(url=url, headers=self.header).json().get("data")
        if not ciddata:
            raise Exception("Cid Api 访问异常... Detail:" + str(ciddata))
        #data = requests.get(url).json()['data']
        title = ciddata['title']
        cid = ciddata['pages'][p - 1]['cid']
        return str(cid), title

    def getInformation(self, bvList):
        infoList = []
        for bvid in bvList:
            item = []
            if len(bvid) == 12:
                cid, title = self.getCidAndTitle(bvid)
                item.append(bvid)
            else:
                cid, title = self.getCidAndTitle(bvid[:12], int(bvid[13:]))
                item.append(bvid[:12])
            item.append(cid)
            item.append(title)
            # item.append('mool_' + str(id + 1))
            infoList.append(item)
        # print(infoList)

        return infoList

    def getMutipleInformation(self, bvid):
        url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
        data = requests.get(url).json()['data']
        # base_title = data['title']
        infoList = []
        for page in data['pages']:
            # print(page)
            title = page['part']
            cid = str(page['cid'])
            item = [bvid, cid, title]
            infoList.append(item)

        return infoList
