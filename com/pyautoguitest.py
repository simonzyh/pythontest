import pyautogui

# !/usr/bin/python
# encoding: utf-8
import time
import pyautogui
import pyperclip
import time
import os




def sendmsg(user,msg):
    choicuser(user)
    pyperclip.copy(msg)
    pyautogui.hotkey('Ctrl', 'v')
    pyautogui.press('enter')


def sendpic(user,pic):
    choicuser(user)
    choicpic(pic)
    pyautogui.hotkey('Ctrl', 'v')
    pyautogui.press('enter')

def choicuser(user):
    # pyautogui.hotkey('shiftleft', 's')
     pyautogui.hotkey('altleft', 'z')
     pyperclip.copy(user)
     pyautogui.hotkey('Ctrl', 'v')
     pyautogui.press('enter')


def choicpic(path):
     os.system(path)
     time.sleep(0.7)
     pyautogui.hotkey('Ctrl', 'c')
     pyautogui.hotkey('altleft', 'F4')


def send():
    pyautogui.hotkey('Ctrl', 'v')
    pyautogui.press('enter')


users=['001','002','003','004','005','006','007']

def sharelink():
    pyautogui.hotkey('altleft', 'z')
    pyautogui.typewrite('001')
    pyautogui.press('enter')
    x,y=pyautogui.position()
    print(x,y)
    pyautogui.moveTo(909,447)
    pyautogui.click()
    pyautogui.hotkey('Ctrl', 'c')

    for u in users:
      time.sleep(2)
      pyautogui.hotkey('altleft', 'z')
      pyautogui.typewrite(u)
      pyautogui.press('enter')
      pyautogui.hotkey('Ctrl', 'v')
      pyautogui.press('enter')

pyautogui.PAUSE = 0.5
count=0
time.sleep(3)
sharelink()
print('当前时间为：'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

while(count<5):
 for u in users:
  time.sleep(2)
  msg=' 你好， 测试100条时间当前时间为：'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
  sendmsg(u,msg)
  sendpic(u,'logo.png')

 count=count+1


print('当前时间为：'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
