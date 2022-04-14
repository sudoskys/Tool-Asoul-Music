import time
import os
from mods.urlGet import infoGet
from mods.fileGet import fileGet
from pathlib import Path
# from tqdm.notebook import trange

# 接受数据格式如下
'''
BVList=[
'BV1QL4y1g7sA','BV1QP4y1F7La',
#     'BV1dA411L7Kj','BV1aK4y1a7sd','BV1wf4y1k7as',
#     'BV1CK4y1W7Cc','BV12X4y1K7Ys','BV1Fz4y167Ru',
#     'BV17y4y167xu','BV1wD4y1X7fP','BV1wV41117GP']
'''


class Upload(object):
    def __init__(self):
        self.IsDebug = False
    #    def callback(self,filePath):
    #        print(filePath)
    def deal_audio_list(self, bvid_list, savePath, callb):
        infoList = infoGet().getInformation(bvid_list)
        sath = str(Path().cwd()) + savePath
        for item in infoList:
            # print('Downloader Start!')
            st = time.time()
            musicPath = fileGet().getAudio(item, sath)
            bvid, cid, title = item[0], item[1], item[2]
            # callb.postAudio(musicPath, title + '\n' + 'https://www.bilibili.com/video/' + str(bvid) + "\n #MusicFinder #Automatic #V5 ", title)  # +
            # '\nSync  ' + '<a href="' + syncurl + '">link here</a>', mtitle)
            ed = time.time()
            # print('Download Finish! Time consuming:',str(round(ed-st,2))+' seconds')


# Upload().deal_audio_list(BVList,'/music')


'''
class onedrive(object):
    # robotPush(token,groupID).postAudio(fileroad,info,name):
    def __init__(self, pri, zuhuid, keyid):
        import base64
        import mods.rsatool as rastool
        with open(useTool().filesafer('data/public.cer'), 'r', encoding='utf-8') as f:
            pub = f.read()
        alice_call = {
            'pub': pub,
            'pri': str(base64.b64decode(pri), "utf-8"),
        }
        self.zras = rastool.RsaUtil(mode="STR", **alice_call)
        self.zuhuid = zuhuid
        self.keyid = keyid
        # import json
        with open(useTool().filesafer('o365_token.txt'), 'r', encoding='utf-8') as f:
            token = f.read()
        tokens = self.zras.decrypt_by_private_key(str(token))
        tokens = str(base64.b64decode(tokens), "utf-8")
        with open(useTool().filesafer("o365_token.txt"), 'w+') as f:
            # f.write(json.dumps(self.token))
            f.write(tokens)

    def upload(self, _path):
        from O365 import Account
        credentials = (self.zuhuid, self.keyid)
        account = Account(credentials=credentials)  # credentials=credentials)
        storage = account.storage()
        my_drive = storage.get_default_drive()
        pro = my_drive.get_item_by_path('/share/Music')
        pro.upload_file(item=_path)
        return useTool().filesafer("o365_token.txt")

    def lock_token(self):
        import base64
        with open(useTool().filesafer("o365_token.txt"), 'r', encoding='utf-8') as f:
            tokens = f.read()
        tokens = str(base64.b64encode(tokens.encode("utf-8")), "utf-8")
        con = self.zras.encrypt_by_public_key(tokens).decode('utf-8')
        with open(useTool().filesafer("o365_token.txt"), 'w+') as f:
            f.write(con)
'''


# 机器人实例
class robotPush(object):
    # robotPush(token,groupID).postAudio(fileroad,info,name):
    def __init__(self, token, ID):
        import telebot
        self.BOT = telebot.TeleBot(token, parse_mode="HTML")  # You can set parse_mode by default. HTML or MARKDOWN
        self.objectID = ID

    def sendMessage(self, msg):
        self.BOT.send_message(self.objectID, str(msg))

    def postVideo(self, file, source, name):
        if os.path.exists(file):
            video = open(file, 'rb')
            self.BOT.send_video(self.objectID, video, source, name, name)
            # '#音乐MV #AUTOrunning '+str(source)+"   "+name
            # 显示要求为MP4--https://mlog.club/article/5018822
            # print("============Already upload this video============")
            video.close()
            return file

    def postAudio(self, file, source, name):
        if os.path.exists(file):
            audio = open(file, 'rb')
            self.BOT.send_audio(self.objectID, audio, source, name, name)
            # '#音乐提取 #AUTOrunning '+str(source)+"   "+name
            # print("============ALready upload this flac============")
            audio.close()
            return file
