from urllib import request
import os

response = request.urlopen("http://www.baidu.com/")  # 打开网站
print(response.readline())
print(os.getcwd())
print(os.getcwdu())
