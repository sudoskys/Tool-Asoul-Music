#utf-8
import time
import os
import shutil

from mods.urlGet import infoGet
from mods.fileGet import fileGet
from pathlib import Path


BVList=[
'BV1QL4y1g7sA','BV1QP4y1F7La',
#     'BV1dA411L7Kj','BV1aK4y1a7sd','BV1wf4y1k7as',
#     'BV1CK4y1W7Cc','BV12X4y1K7Ys','BV1Fz4y167Ru',
#     'BV17y4y167xu','BV1wD4y1X7fP','BV1wV41117GP'
 ]

def deal_audio(bvid_list,savePath):    
    print('Downloader Start!')
    sath = str(Path().cwd()) + savePath
    st = time.time()
    fileGet().getAudio(infoGet().getInformation(bvid_list), sath)
    ed = time.time()
    print('Download Finish All! Time consuming:',str(round(ed-st,2))+' seconds')

deal_audio(BVList,'/music')
