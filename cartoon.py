#!/usr/bin/python
#coding=utf-8

######################################################################################################
# datetime: 20220206                                                                                 #
# author: fly                                                                                        #
# application: get many pictures via links                                                           #
# from give links get images links and names, and save images with assign path and name              #
######################################################################################################

# 懒加载
# 响应超时
# javascript动态生成

import os
import re
import sys
import time
# import typer
import logging                    # 调试中间输出内容适用logging，最终面向用户的输出结果适用print()
import requests                   # using requests replace urllib.request to get http
from mylog import getlog
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

# 命令行接口工具
# cli = typer.Typer()

# DEBUG的log
# logger = getlog(logging.DEBUG)
logger = getlog(logging.INFO)

# 漫画爬虫类
class Cartoon:

    def __init__(self, super_url, base_path):
        self.url_list = [super_url]
        # self.url = super_url
        self.path = base_path
        self.header = {
                'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4758.82 Safari/537.36 '
                }

    # __call__类的实例可以作为函数调用，实现获取图片的最终目的
    def __call__(self):
        self.get_chapter_url()
        while self.url_list:
            i = 1
            for pic_url in self.mkdir_of_chapter_and_get_pic_url():
                logger.info("download image from "+pic_url)
                self.download_image(pic_url, str(i))
                i += 1
                time.sleep(0.01)
            time.sleep(1)
    
    # 根据super url获取章节地址
    def get_chapter_url(self):
        super_url = self.url_list.pop()
        resp = requests.get(super_url)
        res = BeautifulSoup(resp.text, 'lxml')
        chapter = res.find_all('div', "detail-list-item")
        base_url = '/'.join(super_url.split('/')[:3])
        for sec in chapter:
            url = base_url+sec.a['href']
            self.url_list.append(url)
            # yield sec.a['href']

    # 创建章节目录，获取章节所有图片
    def mkdir_of_chapter_and_get_pic_url(self):
        url = self.url_list.pop()
        logger.info("chapter url is "+url)
        # logger.debug("chapter url is "+url)
        resp = requests.get(url, self.header)
        res = BeautifulSoup(resp.text, 'lxml')
        url_string = res.find_all("script")[1].string 
        url_list = re.findall(r"(https.*?jpg)", url_string)

        chapter = res.find('p', "view-fix-top-bar-title").string
        logger.info("chapter is "+chapter)

        path = self.path.split('/')[:-1] + [chapter]
        self.path = '/'.join(path)
        # logger.info(self.path)
        # ensure path is exist
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            logger.info("mkdir "+self.path+" success")

        return url_list

    # download picture from url
    def download_image(self, pic_url, name):

        sess = requests.Session()
        sess.mount('http://', HTTPAdapter(max_retries=5))              # 重试5次
        sess.mount('https://', HTTPAdapter(max_retries=5))

        try:
            pic = sess.get(pic_url, headers=self.header, timeout=15)   # 15秒超时

            # compose name with path and original name
            name = os.path.join(self.path, name)
            with open(name, 'wb') as f:
                f.write(pic.content)      # 图片
            logger.info("download image {name} success".format(name=name))
        except Exception as e:
            print(e)
        # print("download image {link} success".format(link))

if __name__ == "__main__":
    # 单元测试，实际应用
    # sys.argv 包含脚本名称的参数列表
    try:
        super_url, base_path = sys.argv[1:]   # 文件存储地址带/方便切分
        logger.info("get images from "+super_url+" and save to "+base_path)
        cartoon = Cartoon(super_url, base_path)
        cartoon()
    except Exception as e:
        print(e)
    else:
        print("download all images success")
