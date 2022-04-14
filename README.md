

![a](https://s1.328888.xyz/2022/04/13/fPSGZ.jpg)

------------------------------------

<p align="center">
  <a href="https://img.shields.io/badge/LICENSE-Apache2-ff69b4"><img alt="License" src="https://img.shields.io/badge/LICENSE-Apache2-ff69b4"></a>
  <img src="https://img.shields.io/badge/USE-python-green" alt="PYTHON" >
  <img src="https://img.shields.io/badge/Version-220415-9cf" alt="V" >
  <a href="https://azz.net/ly233"><img src="https://img.shields.io/badge/Sponsor-Alipay-ff69b4" alt="SPONSOR"></a>
</p>


<h2 align="center">Tool-Asoul-Music</h2>

**[中文](README.md)**

*A tool for telegram channal delivery,and it can help you to deliver the audio file by asking bilibili api.*

*自动抓取音乐二创并推送，支持手动模式。*

重构自上游项目 github.com/sudoskys/BiliBiliVideoToMusic



## 开始

### 1. 安装要求
**Python 3.7 或更高版本** 

```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- FFmpeg环境 [ffmpeg](https://ffmpeg.org/download.html#get-packages)。
（仓库Action使用 https://github.com/marketplace/actions/setup-ffmpeg ）

* 本地使用运行 `pip install -r requirements.txt`来安装必要包


### 2. 准备
### 本地部署运行
**配置程序设置文件**

*USE config.yaml*
```yaml
Running: true
channalId: -10086
onedrive: {statu: open, target: authkey/onedrive.token}
search: {duration: '1', keyword: ASOUL 原创曲, order: pubdate, page: '1', search_type: video,  tids_1: '3', tids_2: '28'}

```

- 配置搜索字段
```yaml
search: {duration: '1', keyword: ASOUL 原创曲, order: pubdate, page: '1', search_type: video,  tids_1: '3', tids_2: '28'}
```
- 配置Onedrive同步
```yaml
onedrive: {statu: open, target: authkey/onedrive.token}
```

- 配置音乐频道推送服务
1.申请一个Bot,向BotFather索取Token
2.使用ID机器人查看目标频道ID
3.将机器人添加至频道并只赋予发消息权限
```yaml
channalId: -youchannalIDnumberhere
```

### 托管 Github Action （不推荐）
* Fork 本仓库并设置secrets
Tips: 如果您使用action部署，建议只设置提取flac。
配置此action，需要在环境内加secrets，一个是 githubtoken，一个是 email。（申请地址[github openapi token](https://github.com/settings/tokens/new)


*Add Repository secrets*
```
${{ secrets.key }}
```

*Add Environment secrets*
```
${{ secrets.GITHUB_TOKEN }}
${{ secrets.GITHUB_EMAIL }}

```

* 说明
Github action每天6:20运行一次流程（需要手动设置），仓库主人加星也会触发流程.

**运行**

```shell
python main.py
```

### Colab 调试

```
!rm -f -r /content/*
!git clone https://github.com/sudoskys/Tool-Asoul-Music
!rsync -r /content/Tool-Asoul-Music/* /content/
!python -m pip install --upgrade pip
!pip3 install -r requirements.txt
```

## 实现逻辑

分离了请求与推送，采用队列制，可以方便开发与扩展。



### 目录结构描述
```
.
├── authkey
│    └── onedrive.token  // onedrive的token密文
├── config.yaml  // 配置文件
├── data
│    └── history.yaml   // 历史记录
├── LICENSE  // 协议
├── main.py  // 主程序
├── mods
│    ├── core.py  // 基础函数
│    ├── fileGet.py  // 文件获取
│    ├── locker.py   // 加密安全算法
│    ├── Runner    // api相关
│    │    └── renew.py
│    ├── uploadFile.py  // 推送
│    └── urlGet.py  // 解析cid
├── rank   // 队列实现
│    └── waiter
│    │   └── init.lck  // 定位目录的锚点
│    └── content.yaml  // 队列索引
├── README.md   //介绍
└── requirements.txt 

```

## TODO
- [x] 重构代码结构
- [x] 优化冗余代码
- [x] 优化实现流程
- [ ] 支持手动添加
- [ ] 支持同步OD盘
- [ ] 重构 1 次
- [ ] 重构 2 次
- [ ] 重构 3 次

## 鸣谢

- [BilibiliDownloader](https://github.com/liuyunhaozz/bilibiliDownloader)|下载部分参考|
- [O365](https://github.com/O365/python-o365) |微软云盘同步实现|
- [RSShub](https://docs.rsshub.app/) |数据源RSS|



------------------------------

![counter](https://count.getloli.com/get/@sudoskys-github-AsoulMusic?theme=moebooru)

------------------------------

>支持 https://azz.net/ly233

