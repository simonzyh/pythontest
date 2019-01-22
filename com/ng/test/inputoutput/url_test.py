import os
import time
from urllib import request
from bs4 import BeautifulSoup


# 读取文件，读取以行为单位，每一行是列表里的一个元素
def readJarsLink(url, path, runjar):
    response = request.urlopen(url)  # 打开网站
    bsObj = BeautifulSoup(response.read())
    jarLinks = []

    links = bsObj.findAll("a")
    for link in links:
        if ('jar' == link.string[-3:]):
            jarLinks.append(link['href'])
    jarLinks.sort()

    ###最新的jar名称
    jarname = jarLinks[-1].split('/')[-1]
    ##切换工作目录
    os.chdir(path)
    ##下载文件
    jarUrl = jarLinks[-1]
    os.system("wget " + jarUrl)
    print('下载jar包:' + jarUrl)

    startJvm(runjar, jarname)
    return jarLinks


def startJvm(runjar, newjar):
    os.system("mv " + newjar + " " + runjar)
    print('修改jar:' + runjar + ' ' + newjar)
    os.system(" ./start.sh ")


## 提取jar链接
while True:
    readJarsLink(
        "http://192.168.20.6:8081/nexus/content/repositories/snapshots/com/orko/distribution/distribution-admin-web/0.0.1-SNAPSHOT/",
        '/home/www/app/distribution-admin', 'distribution-admin-web-0.0.1-SNAPSHOT.jar');
    readJarsLink(
        "http://192.168.20.6:8081/nexus/content/repositories/snapshots/com/orko/distribution/distribution-api/0.0.1-SNAPSHOT/",
        '/home/www/app/distribution-api', 'distribution-api-0.0.1-SNAPSHOT.jar');
    time.sleep(300)
