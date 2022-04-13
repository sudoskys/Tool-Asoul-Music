#utf-8
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
data = yamler().read(str(Path.cwd())+"/config.yaml")
looking=data.get("search") # 探测器传入的数据
botToken = str(data.get('botToken')) # 机器人token ，从botfather那里拿
channalId = str(data.get("channalId")) # 从getid bot那里看

if data.get('Lock'):
    print("unLocking")
    from mods import locker
    import sys
    keyword = sys.argv[1]
    botToken=AESlock().decrypt(str(keyword),botToken.encode('utf-8'))
    


# 探测
RES = apiRenew().apiInit(looking)
if RES:
    key = apiRenew().doData(RES)
    if key:
        print(key)
        #apiRenew().cancelTask(key)



# 处理
task = yamler().read("rank/content.yaml")
## 得到任务
if task:
    for i, k in enumerate(task):
        task_todo = yamler().read(task.get(k))
        #mian(lme, ath, k)
        if not all([botToken,channalId]):
            raise Exception("参数不全!", lmain)
        else:
            # 构建机器人实例
            push = robotPush(botToken, channalId)
            # sync = onedrive(apptoken, appid, appkey)
            time.sleep(2)
            if not task_todo:
                print("Today nothing to do")
                # sync.lock_token()
                shutil.rmtree(os.getcwd() + '/music/', ignore_errors=False, onerror=None)  # 删除
            else:
                print(task_todo)
                # 传入
                bvlist=[]
                if isinstance(task_todo, dict):
                    for n, u in enumerate(data):
                        bv=str(data.get(u).get("bvid"))
                        bvlist.append(bv)
                else:
                    for n, u in enumerate(data):
                        bv=str(u.get("bvid"))
                        bvlist.append(bv)
                try:
                    Upload().deal_audio_list(bvlist, '/music', push)
                    #dealUrl(n, urls, push, sync)
                except BaseException as arg:
                    push.sendMessage('Failed post ' + n + '\n Url:' + u + '\n Exception:' + str(arg))
                    # mLog("err", "Fail " + n + '  -' + u).wq()
                # sync.lock_token()
                from mods.Runner.renew import apiRenew
                apiRenew().cancelTask(key)
                shutil.rmtree(os.getcwd() + '/music/', ignore_errors=False, onerror=None)  # 删除存储的视频文件


# channal id ,please use @getidsbot get this value!
