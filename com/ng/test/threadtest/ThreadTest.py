#!/usr/bin/python3
from  com.ng.test.threadtest import ThreadExec
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
      print('currentThread='+str(threading.currentThread))
      print('activeCount='+str(threading.activeCount))


# 创建两个线程
try:
   _thread.start_new_thread( ThreadExec.print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( ThreadExec.print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")


while 1:
   pass
