# **基于scrapy框架的闲鱼二手网站信息抓取** #

## 功能 
- 全站爬虫
- 支持mongodb数据库的写入
- 自动更换用户代理
- 根据请求频率自动限速

## 环境要求
- Python 3.0+
- Scrapy 1.3+

## 我的开发环境
- Anaconda 1.6.5
- scrapy 1.3.3

## 安装步骤
1. `git clone https://github.com/xiaofang-git/xianyu.git `  #克隆项目到本地

2. `cd ershou` # 进入项目文件

3. `scrapy list` # 查看是否存在xinyu的spider

4. `pip install fake_useragent pymongo` # 安装除了scrapy之外还需要的第三方库文件
 - fake_useragent =>实现自动更换用户代理
 - pymongo => 链接数据库
 > fake_useragent使用过程中或许会出现报错的情况，但是不会导致程序退出
 5. `scrapy crawl xianyu`#启动爬虫文件就可以在命令行中查看抓取到的数据

 ## 修改配置

 - 常规设置请参考scrapy文档修改setting文件
 - 程序已经实现了mongo数据库的写入功能，请修改setting文件中pipline的设置。将`ershou.pipelines.ErshouPipeline`注释掉，而将`ershou.pipelines.ErshouPipeline`取消注释
 >`ITEM_PIPELINES = {
    'ershou.pipelines.ErshouPipeline': 300,
    #'ershou.pipelines.WriteMongo': 3
}`

## 联系方式
   <fang.1995@outlook.com> 

