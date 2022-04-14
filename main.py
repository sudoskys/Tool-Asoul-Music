# encoding: utf-8
# 本文件负责启动流程，通过tasker协调分离任务。
import time
import os
import shutil

from mods.Runner.renew import apiRenew
from mods.core import yamler
from mods.uploadFile import robotPush
from mods.uploadFile import Upload
from pathlib import Path

# 加载配置
data = yamler().read(str(Path.cwd()) + "/config.yaml")
looking = data.get("search")  # 探测器传入的数据
botToken = str(data.get('botToken'))  # 机器人token ，从botfather那里拿
channalId = str(data.get("channalId"))  # 从getid bot那里看
rss = str(data.get("RSS"))  # 从getid bot那里看
if rss.get('statu'):
    rssAddress = rss.get('RssAddressToken')
        

if data.get('Lock'):
    print("unLocking")
    from mods.locker import AESlock
    import sys
    keyword = sys.argv[1]
    botToken = AESlock().decrypt(str(keyword), botToken.encode('utf-8'))
    if rss.get('statu'):
        rssAddress = AESlock().decrypt(str(keyword), rss.get('RssAddressToken').encode('utf-8'))
        

# 探测
RES = apiRenew().apiInit(looking)
if RES:
    key = apiRenew().doData(RES)
    if key:
        print('resign new task--> '+key)
        # apiRenew().cancelTask(key)



from mods.rssKit import rssParse
Path(os.getcwd() + '/music/').mkdir(parents=True, exist_ok=True)
items=rssParse().getItem(rssAddress)
rssBvidItem=[]
if items:
    for k,v in items.items():
        rssBvidItem.append(rssParse.get_bili_id(str(v))[0])
try:
    if not len(rssBvidItem)==0:
        Upload().deal_audio_list(rssBvidItem, '/music', push)
    else:
        print("RSS No New Data")
except BaseException as arg:
    robotPush(botToken, channalId).sendMessage('Failed post ' + str(bvlist) + '\n Exception:' + str(arg))
finally:
    shutil.rmtree(os.getcwd() + '/music/', ignore_errors=False, onerror=None)  # 删除
    # mLog("err", "Fail " + n + '  -' + u).wq()
#rssgeter


# 处理
task = yamler().read("rank/content.yaml")
# 得到任务
if task:
    for i, k in enumerate(task):
        task_todo = yamler().read(task.get(k))
        # mian(lme, ath, k)
        if not all([botToken, channalId]):
            raise Exception("参数不全!")
        else:
            # 构建机器人实例
            push = robotPush(botToken, channalId)
            Path(os.getcwd() + '/music/').mkdir(parents=True, exist_ok=True)
            # sync = onedrive(apptoken, appid, appkey)
            if not task_todo:
                print("Tasker nothing to do")
                apiRenew().cancelTask(k)
                # sync.lock_token()
                shutil.rmtree(os.getcwd() + '/music/', ignore_errors=False, onerror=None)  # 删除
            else:
                # print(task_todo)
                # print(type(task_todo))
                # 传入
                bvlist = []
                if isinstance(task_todo, dict):
                    for n, u in enumerate(task_todo):
                        # bv = str(task_todo.get(u).get("bvid"))
                        bvlist.append(u)
                time.sleep(1)
                try:
                    Upload().deal_audio_list(bvlist, '/music', push)
                except BaseException as arg:
                    push.sendMessage('Failed post ' + str(bvlist) + '\n Exception:' + str(arg))
                    # mLog("err", "Fail " + n + '  -' + u).wq()
                else:
                    apiRenew().cancelTask(k)
                # sync.lock_token()
                shutil.rmtree(os.getcwd() + '/music/', ignore_errors=False, onerror=None)  # 删除存储的视频文件

# channal id ,please use @getidsbot get this value!
