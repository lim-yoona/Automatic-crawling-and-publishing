import pyautogui as pg
import time
# import time
# pList=[]
# f=open('inputP.txt','r',encoding='utf-8')
# for line in f:
#     pList.append(line.strip('\n'))
# print(pList)
# i=0
# dict={}
# while True:
#     if pList[i]=='#':
#         break
#     dict[pList[i]]=pList[i+1]
#     i=i+2
# print(dict)
# time.sleep(5)
# for i in ['用户名','密码','登录']:
#     pg.click(dict[i][0],dict[i][1])

import pyperclip as pp

w,h=pg.size()
pg.click(w/2,h/2)
pp.copy('你好')
#time.sleep(4)
pg.hotkey('ctrl','v')
pg.typewrite('yyy')