#!/usr/bin/python3

import time;  # 引入time模块
import calendar
import queue

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print('当前时间：'+time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

print(dir(queue))

print(hex(12))

b = divmod(7, 2)
print(type(b))


class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        print('getx')
        return self._x

    def setx(self, value):
        print('setx')
        self._x = value

    def delx(self):
        print('delx')
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


c = C();

c.x;
