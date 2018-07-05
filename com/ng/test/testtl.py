# !/usr/bin/python
# encoding: utf-8

import requests

try:
 apiUrl = 'http://www.tuling123.com/openapi/api'
 data = {
    'key': '8edce3ce905a4c1dbb965e6b35c3834d',
    'info': 'hello',
    'userid': 'wechat-robot'
 }
# 我们通过如下命令发送一个post请求
 r = requests.post(apiUrl, data=data).json()

# 让我们打印一下返回的值，看一下我们拿到了什么
 print(r)
 print(type(r))
 print(r['text'])
except BaseException:
 print('except')
