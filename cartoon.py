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
import time
import logging                    # 调试中间输出内容适用logging，最终面向用户的输出结果适用print()
import requests                   # using requests replace urllib.request to get http
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

# 漫画爬虫类
class Cartoon:

    def __init__(self, superUrl):
        self.url = superUrl
        self.header = {
                'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4758.82 Safari/537.36 '
                }

    def __call__(self):
        resp = requests.get(self.url)
        res = BeautifulSoup(resp.text, 'lxml')
        return res.title
    
    def get_child_link_and_name(self):
        resp = requests.get(self.url)
        res = BeautifulSoup(resp.text, 'lxml')
        # res.find(class_="view-win-list detail-list-select")
        # return res.find_all(href=re.compile("chapter"), target="_blank")   # 同时满足多个条件
        return res.find_all(href=re.compile("chapter"), target="_blank").string

    def get_image_link(self, child_link):
        resp = requests.get(child_link)
        res = BeautifulSoup(resp.text, 'lxml')
        return resp

    # download picture from url, which save to path/name
    def download_image(self, link, path, name):
        # ensure path is exist
        if not os.path.exists(path):
            os.makedirs(path)
        # compose name with path and original name
        name = os.path.join(path, name)

        res = requests.get(link, headers=self.header)

        # response ok
        if res.status_code != 200:
            print("download image {link} error ".format(link))
        # write content to a file 
        with open(name, "wb") as img:
            img.write(res.content)
        print("download image {link} success".format(link))

if __name__ == "__main__":
    # 单元测试，实际应用
    # 命令行支持
    super_url = None
    cartoon = Cartoon(super_url)
