from mods.core import yamler
from pathlib import Path
class apiRenew(object):
    def __init__(self):
        self.END = False
        self.header = {
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

    def clearTask(self, files):
        m=Path('rank/waiter/init.lck')
        file_list[path for path in m.glob('*.yaml')]
        try:
            for i, k in enumerate(file_list):
                Path(k).unlink(missing_ok=True)
            Path("rank/content.yaml").unlink(missing_ok=True)
        except Exception as err:
            print(err)
        else:
            pass

    def raiseTask(self, data):
        import time
        times = str(time.strftime("%Y%m%d%H%M", time.localtime()))
        yamler().save("rank/waiter/" + times + ".yaml", data)
        info = yamler().read("rank/content.yaml")
        if not info:
            info = {}
        info[times] = ("rank/waiter/" + times + ".yaml")
        yamler().save("rank/content.yaml", info)
        return times

    def cancelTask(self, keys):
        lists = yamler().read("rank/content.yaml")
        if lists:
           if lists.get(keys):
              m= Path(lists.get(keys))
              if m.is_file(): 
                 m.unlink(missing_ok=True)
              if info.pop(keys):
                 yamler().save("rank/content.yaml", info)

    def doData(self, newer):
        import time
        import random
        def random_sleep(mu=3, sigma=1.7):
            """正态分布随机睡眠
            :param mu: 平均值
            :param sigma: 标准差，决定波动范围
            """
            secs = random.normalvariate(mu, sigma)
            if secs <= 0:
                secs = mu  # 太小则重置为平均值
            time.sleep(secs)

        random_sleep()
        # 强制间隔防止被Ban
        older = yamler().read("data/history.yaml")
        if not older:
            older = {}
        if isinstance(newer, dict):
            # logging.debug(older)
            if len(list(older)) != 0:
                deal = {i: newer.get(i) for i in newer.keys() if i not in older.keys()}
                # total = older.update(newer)
                total = {**older, **newer}
            else:
                total = newer
                deal = newer

            yamler().save("data/history.yaml", total)
            print(deal) # 打印需要添加的条目
            # 注册任务
            key = self.raiseTask(deal)
            return key
        else:
            #logger.info("NEED DICT")
            print("NEED DICT")
            return False

    def apiInit(self, datas):
        import json
        import requests
        URLs = "http://api.bilibili.com/x/web-interface/search/type"
        # data = {"key":"value"}
        response = requests.get(url=URLs, params=datas, headers=self.header)
        if response.status_code == 200:
            content = response.text
            json_dict = json.loads(content)
            # logger.debug(json_dict)
            if json_dict['message'] == "0":
                if json_dict['data'].get("result"):
                    try:
                        res = json_dict['data'].get("result")
                        """
                        投币>20
                        &点赞>1000
                        &投币*2>收藏
                        &投币/点赞>0.3
                        or 
                        播放>2w
                        """
                        # logging.debug(res)
                        result = {}
                        for index, item in enumerate(res):
                            video_object = {}
                            title = item.get("title")
                            titles = title.replace('<em class="keyword">', '').replace('</em>', '')
                            char = '\:*?"<>|/'
                            for acao in char:
                                titles = titles.replace(acao, "_")
                            # logging.debug(titles)
                            video_object['title'] = titles
                            video_object['bvid'] = item.get("bvid")
                            video_object['review'] = item.get("review")
                            video_object['favorites'] = item.get("favorites")
                            video_object['play'] = item.get("play")
                            video_object['like'] = item.get("like")
                            video_object['tag'] = item.get("tag")
                            if video_object['title'].find("原创曲") != -1 or video_object['tag'].find("原创歌曲") != -1 or \
                                    video_object['tag'].find("原创曲") != -1 or video_object['play'] > 20000 or \
                                    video_object['favorites'] * 5 > video_object['like']:
                                result[video_object['bvid']] = video_object
                                # return result
                            else:
                                if video_object['favorites'] > 1000:
                                    result[video_object['bvid']] = video_object
                        #logger.debug
                        print(result)
                        return result
                    except LookupError as err:
                        #logger.error
                        print(err)
                        return False
                else:
                    #logger.info
                    print("NO data" + str(json_dict))
                    self.END = True
                    return False
            else:
                #logger.debug
                print("NO Data Code" + str(json_dict))
                return False
        else:
            #logger.debug
            print("NET CODE  " + str(response.status_code))
            return False


