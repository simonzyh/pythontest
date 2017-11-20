#!/usr/bin/python3

import _thread
import time
import threading
# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
   print('currentThread=' + str(threading.currentThread))
   print('activeCount=' + str(threading.activeCount))