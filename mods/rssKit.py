# encoding: utf-8
import feedparser
import os
import json
# ren sheng ku duan ,bu yao yong python ,
class rssParse(object):
    def __init__(self,path='RssData.json'):
        self.parseMode = True
        self.dataPath = path
        if not os.path.exists(path): 
            with open(path, 'w+') as f:
                json.dump({}, f)

    def setUrl(self, url, save):
        fp = feedparser.parse(url)
        name_list = []
        target_list = []
        for m in fp.entries:
            # print('T:',m.title)
            # print('U:',m.links[0].href)
            name_list.append(m.title)
            target_list.append(m.links[0].href)
        items = dict(zip(name_list, target_list))
        if save:
            with open(self.dataPath, 'w+') as f:
                json.dump(items, f)
        return items

    def getItem(self,url,Save=True):
        older={}
        with open(self.dataPath, 'r') as f:
            older = json.load(fp=f)
        newer = self.setUrl(url,Save)
        if len(older)==0:
            return newer
        else:
            result_key = newer.keys() - older.keys()
            result = {name: value for name,value in newer.items() if name in result_key}
            if not result:
                result={}
            return result

    def getFullItem(self, url, Save=False):
        return self.setUrl(url,Save)

    @staticmethod
    def get_bili_id(bili_url):
        import re
        """ 判断传入链接的类型,并获取id """
        url_re = self.b32_url(bili_url) if "b23.tv" in bili_url else bili_url
        list_re = re.split("/", url_re)
        url_text_re = list_re[len(list_re) - 1]
        # print(url_text_re)  # re 的链接！！
        bili_id_tf = [True if tf in url_text_re else False for tf in ["?", "#"]]
        bili_id = re.findall(r".+?[?|#]", url_text_re)[0][:-1] if any(bili_id_tf) else url_text_re
        if bili_id[0:2] == "cv" or len(list(bili_id)) < 9:  # 判断专栏
            bili_id = bili_id[2:] if bili_id[0:2] == "cv" else bili_id
            bili_type = 2
        else:  # 判断动态或视频
            bili_type = 0 if bili_id[0:2] == "BV" else 1
        # print(bili_id) # id在这里
        """ 0.视频 1.动态 2.专栏 """
        return bili_id, bili_type  # id, type