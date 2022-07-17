# encoding: utf-8
# 本文件负责启动流程，通过tasker协调分离任务。
import time
import os
import shutil

#import sys
#sys.path.insert(0, '/root/Tool-Asoul-Music')

from mods.Runner.renew import apiRenew
from mods.core import yamler
from mods.core import doTarGz
from mods.uploadFile import robotPush
from mods.uploadFile import Upload
from pathlib import Path

# 加载配置
Nowtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
WrongGet=[] #日志
HaveNew=False
data = yamler().read(str(Path.cwd()) + "/config.yaml")
looking = data.get("search")  # 探测器传入的数据

dataCallback = data.get("DataCallback")  # 是否启用数据发送备份

botToken = str(data.get('botToken'))  # 机器人token ，从botfather那里拿
channalId = str(data.get("channalId"))  # 从getid bot那里看
rss = (data.get("RSS"))  # 从getid bot那里看
if rss.get('statu'):
    rssAddress = rss.get('RssAddressToken')
if dataCallback.get('statu'):
    userId = dataCallback.get('UserIdToken')
        


if data.get('Lock'):
    print("加密模式启用中--")
    from mods.locker import AESlock
    import sys
    keyword = sys.argv[1]
    botToken = AESlock().decrypt(str(keyword), botToken.encode('utf-8'))
    if rss.get('statu'):
        rssAddress = AESlock().decrypt(str(keyword), rss.get('RssAddressToken').encode('utf-8'))
    if dataCallback.get('statu'):
        userId = AESlock().decrypt(str(keyword), dataCallback.get('UserIdToken').encode('utf-8'))
        




# 推送机器人
push = 0
#RSS

from mods.rssKit import rssParse
if rss.get('statu'):
    print("RSS启用中--")
    Path(os.getcwd() + '/music/').mkdir(parents=True, exist_ok=True)
    items=rssParse(path=os.getcwd()+'/data/RssData.json').getItem(rssAddress)
    rssBvidItem=[]
    if items:
        for k,v in items.items():
            rssBvidItem.append(rssParse.get_bili_id(str(v))[0])
    try:
        if not len(rssBvidItem)==0:
            HaveNew=True
            Upload().deal_audio_list(rssBvidItem, '/music', push ,local=True)
        else:
            print("RSS No New Data")
    except BaseException as arg:
        #push.sendMessage('Failed post ' + str(bvlist) + '\n Exception:' + str(arg))
        WrongGet.append(str(Nowtime)+'\n 任务错误' + str(bvlist) + str(arg))
    finally:
        pass
        #shutil.rmtree(os.getcwd() + '/music/', ignore_errors=False, onerror=None)  # 删除
        # mLog("err", "Fail " + n + '  -' + u).wq()
    #rssgeter
else:
    print("RSS已经关闭--")



print(WrongGet)
