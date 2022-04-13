# Tool-Asoul-Music


![a](https://s1.328888.xyz/2022/04/13/fPSGZ.jpg)

------------------------------------


[![Apache License 2.0 License](https://img.shields.io/badge/LICENSE-Apache2-ff69b4)](https://github.com/sudoskys/Tool-Asoul-Music/blob/main/LICENSE)  ![u](https://img.shields.io/badge/USE-python-green)   [![s](https://img.shields.io/badge/Sponsor-Alipay-ff69b4)](https://azz.net/ly233) 

![v](https://img.shields.io/badge/Version-220415-9cf)   **[中文](README.md)**


*A tool for telegram channal delivery,and it can help you to deliver the audio file by asking bilibili api.*

*自动抓取音乐二创并推送，支持手动模式。*

重构自上游项目 BiliBiliVideoToMusic



## 开始

### 1. 安装要求
**Python 3.7 或更高版本** 
```

python -m pip install --upgrade pip
pip install -r requirements.txt

```

- FFmpeg环境 [ffmpeg](https://ffmpeg.org/download.html#get-packages)。
（仓库Action使用 https://github.com/marketplace/actions/setup-ffmpeg ）

* 本地使用运行 `pip install -r requirements.txt`来安装必要包


### 2. 准备
#### 部署运行
**配置程序设置文件**
- 配置目标关键词

- 配置Onedrive同步服务

- 配置音乐频道推送服务
1.申请一个Bot,向BotFather索取Token
2.使用ID机器人查看目标频道ID
3.将机器人添加至频道并只赋予发消息权限

#### 托管 Github Action （不推荐）
* Fork 本仓库并设置secrets
Tips: 如果您使用action部署，建议只设置提取flac。
配置此action，需要在环境内加secrets，一个是 githubtoken，一个是 email。（申请地址[github openapi token](https://github.com/settings/tokens/new)


**Add Repository secrets**
```

```

**Add Environment secrets**
```

```


* 说明
Github action每天6:20运行一次流程，仓库主人加星也会触发流程.




## 实现逻辑(gitPush.py)




### 目录结构描述
```


```

## TODO
- [ ] 重构 1 次
- [ ] 重构 2 次
- [ ] 重构 3 次

## 鸣谢

- [bilibiliDownloader](https://github.com/liuyunhaozz/bilibiliDownloader)|下载部分|
- [O365](https://github.com/O365/python-o365) |微软云盘同步实现|
- [RSShub](https://docs.rsshub.app/) |数据源RSS|



------------------------------
![counter](https://count.getloli.com/get/@sudoskys-github-AsoulMusic?theme=moebooru)



------------------------------

>支持
https://azz.net/ly233

